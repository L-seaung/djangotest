#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from socket import *
""""
该例子加入了线程来处理端口的扫描，从而提高扫描的速度
""""
lock = threading.Lock()#定义全局线程锁
openNum = 0#端口的数量
threads = [] 

def portScaner(host, port):
  global openNum
  try:
      s = socket(AF_INET, SOCK_STREAM)
      s.connect((host, port))
      lock.acquire()#
      openNum += 1
      print('[+] host %s: %d port'%(host, port))
      lock.release()
      s.close()
  except:
      pass

def main():
    setdefaulttimeout(3)
    ip = str(input("enter your want to scaner host port:"))
    for p in range(1, 1024):
        t = threading.Thread(target=portScaner, args=(ip, p))
        threads.append(t)
    for t in threads:
        t.join()
        print("[*] the scaner is complete!")
        print("[*] A total of %d open port"%(openNum))
        
if __name__ == '__main__':
    main()
