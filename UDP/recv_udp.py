from __future__ import print_function
import socket
from contextlib import closing


def main():
    # host = '192.168.1.6'
    host = raw_input("Input IP address: ")
    # port = 9999
    port = int(raw_input("Input Port: "))
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with closing(sock):
        sock.bind((host, port))
        while True:
            print(sock.recv(bufsize))
    return

if __name__ == '__main__':
    main()
