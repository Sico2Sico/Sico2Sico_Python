#coding=utf-8
from socket import *
from threading import  Thread
from time import  sleep


def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0 :
            print("recv[%]:%"%(str(destAddr),recvData))
        else:
            print("客户端已经关闭")
            break
    newSocket.close()


def main():

    serSocket = socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print("主进程开始等待客服端的接入")
            newSocket,destAddr = serSocket.accept()

            print("主线程 接下来 会创建一个新的线程 负责数据处理")
            client = Thread(target=dealWithClient,args=(newSocket,destAddr))
            client.start()

    finally:
        serSocket.close()


if __name__ == '__main__':
    main()
