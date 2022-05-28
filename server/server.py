#!/usr/bin/env python3

import socket
import sys

logfile = sys.argv[1]

f = open(logfile,"a+")
print(f"inside your walls, logfile: {f}")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port).
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.bind(("", 37020))

counter = 0
while True:
    # Thanks @seym45 for a fix
    data, addr = server.recvfrom(1024)
    f.write(f"{counter} received message: {data}\n")
    f.flush()
    counter += 1
