from __future__ import print_function
import socket
import time
from contextlib import closing


def main():
    # host = '192.168.1.56'
    host = raw_input("Input IP address: ")
    # port = 9999
    port = int(raw_input("Input Port: "))
    count = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with closing(sock):
        while True:
            message = 'Hello world : {0}'.format(count).encode('utf-8')
            print(message)
            sock.sendto(message, (host, port))
            count += 1
            time.sleep(1)
    return

if __name__ == '__main__':
    main()
