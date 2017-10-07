#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *

def portScanner(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        print('[+] %d open' % port)
        s.close()
    except:
        print('[-] %d close' % port)
        
def main():
    setdefaulttimeout(3)
    ip = str(input("enter a ip address:"))
    print('[*] scanner the host %s' % ip)
    for p in range(1, 1024):
        portScanner(ip, p)
        
if __name__ == '__main__':
    main()
