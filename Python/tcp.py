#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

HOST = ''
PORT = 56732
BUFFER = 1024
ADDRESS = (HOST, PORT)


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#
tcpServer.bind(ADDRESS)#
tcpServer.listen(5)#设置最大连接数为5
#
while True:
    tcpClient, address = tcpServer.accept()#
    print "the connection from %s" %address
    while True:
        data = tcpClient.recv(BUFFER)#
        if not data:
            break
#
        print data
    tcpClient.close()
tcpServer.close()
