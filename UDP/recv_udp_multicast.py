#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import socket
from contextlib import closing


def main():
    local_address = '192.168.1.5'  # 受信側のPCのIPアドレス
    multicast_group = '239.255.42.99'  # マルチキャストアドレス
    port = 1511
    bufsize = 4096

    with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', port))
        sock.setsockopt(socket.IPPROTO_IP,
                        socket.IP_ADD_MEMBERSHIP,
                        socket.inet_aton(multicast_group) +
                        socket.inet_aton(local_address))
        # while True:
        for i in range(1):
            data = sock.recv(bufsize)
            print(len(data))
            print (data)
    return

if __name__ == '__main__':
    main()
