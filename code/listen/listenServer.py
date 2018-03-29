#coding=utf-8
from socket import *
from time import sleep

# 创建socket链接
tcpSockerServer = socket(AF_INET,SOCK_DGRAM)

# 绑定本地信息
address = ("",88888)
tcpSockerServer.bind(address)

# 设置最大监听数
connNum = int(input("输入最大监听的数:"))
tcpSockerServer.listen(connNum)


while True:
    # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
    newSocket, clientAddr = tcpSockerServer.accept()
    newSocket.send("wdwa",clientAddr)
    sleep(1)