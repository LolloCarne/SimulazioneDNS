import socket 
import sys
import logging

DNS=('localhost',8888)


if __name__ == '__main__':
    s=socket.socket()
    s.connect(DNS)

    try:
        name = sys.argv[-1].strip()
        s.sendall(name.encode())
        porta=int(s.recv(1024).decode())
        if porta == 0:
            print("DNS Server Error")
            s.close()
            exit()
        s.close()
        s=socket.socket()
        s.connect(('localhost',porta))
        s.sendall("GET".encode())
        print(s.recv(1024).decode())          


    
    except KeyboardInterrupt:
        s.close()
        exit()