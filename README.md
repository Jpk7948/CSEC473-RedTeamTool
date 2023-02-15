# CSEC473-RedTeamTool
A red team tool that sends spoofed tcp packets. Supports randomized ip addresses to bloat wireshark traces

In order to spoof from randomized IP addresses enter source ip address using x, y, z, and w as variables.
Each variable will be replaced with a random int from 1 to 254.

Ex.
x.y.z.w,
192.168.x.y,
x.y.55.z

# Arguments

## Required:


### IP
The destination ip address


### Port
The destination port



## Optional


### --source-ip
The IP address to spoof the packets from


### --source-port
The port to spoof the packets from


### --interval
The interval (in seconds) to send each packet.
Each thread will send a packet every x seconds.

Default: 1


### --limit
The amount of packets to send (per thread)

Default: 60


### --threads
The amount of threads to create.

Default: 1