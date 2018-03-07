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

![屏幕快照 2018-03-07 下午3.12.58](/Users/dezhi/Desktop/屏幕快照 2018-03-07 下午3.12.58.png)

![WechatIMG35 3](/Users/dezhi/Desktop/WechatIMG35 3.jpeg)