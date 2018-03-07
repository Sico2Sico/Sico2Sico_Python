## Python 实现客户端 服务端 Socket通信



1 client.py

```python
#coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 准备接收方的地址
sendAddr = ('127.0.0.1', 8888)

while True:
    # 3. 从键盘获取数据
    sendData = raw_input("请输入要发送的数据:")

    # 4. 发送数据到指定的电脑上
    udpSocket.sendto(sendData, sendAddr)

#7. 关闭套接字
udpSocket.close()


```



2 server.py

```python
#coding=utf-8

from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息
bindAddr = ('', 8888) # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

num = 1
while True:

    #3. 等待接收对方发送的数据
    recvData = udpSocket.recvfrom(1024) # 1024表示本次接收的最大字节数

    #4. 将接收到的数据再发送给对方
    udpSocket.sendto(recvData[0], recvData[1])

    #5. 统计信息
    print('已经将接收到的第%d个数据返回给对方,内容为:%s  地址为%s'%(num,recvData[0],recvData[1]))
    num+=1


#5. 关闭套接字
udpSocket.close()
```





## TCP

Client.py

```python
#coding=utf-8
from socket import *

# 创建socket
tcpClientSocket = socket(AF_INET, SOCK_STREAM)

# 链接服务器
serAddr = ("127.0.0.1", 8888)
tcpClientSocket.connect(serAddr)

while True:

    # 提示用户输入数据
    sendData = raw_input("send：")

    if len(sendData)>0:
        tcpClientSocket.send(sendData)
    else:
        break

    # 接收对方发送过来的数据，最大接收1024个字节
    recvData = tcpClientSocket.recv(1024)
    print 'recv:',recvData

# 关闭套接字
tcpClientSocket.close()
```



Server.py

```python
#coding=utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 8888)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
tcpSerSocket.listen(5)

while True:

    # 如果有新的客户端来链接服务器，那么就产生一个信心的套接字专门为这个客户端服务器
    # newSocket用来为这个客户端服务
    # tcpSerSocket就可以省下来专门等待其他新客户端的链接
    newSocket, clientAddr = tcpSerSocket.accept()

    while True:

        # 接收对方发送过来的数据，最大接收1024个字节
        recvData = newSocket.recv(1024)

        # 如果接收的数据的长度为0，则意味着客户端关闭了链接
        if len(recvData)>0:
            print 'recv:',recvData
        else:
            break

        # 发送一些数据到客户端
        sendData = raw_input("send:")
        newSocket.send(sendData)

    # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
    newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpSerSocket.close()

```

