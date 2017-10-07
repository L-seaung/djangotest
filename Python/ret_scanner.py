#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

print '************************'
print '*******author lee*******'
print '************************'


def scanner(ip, port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.send(1024)
        return banner
    except:
        return
        
def main():
    port = int(raw_input('enter a port:'))
    for xport in range(10, 255):
        ip = '172.30.87.' + str(x)
        banner = scanner(ip, port)
        if banner:
            print '[+]' + ip + ':' + banner
        else:
            print '[-]' + ip + ':' + 'no port open of %d' % port
            
if __name__ == '__main__':
    main()
