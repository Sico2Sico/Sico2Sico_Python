#coding= utf-8
import select
from  socket import *
import sys

server = socket(AF_INET,SOCK_STREAM)
locAdder = ('',7788)
server.bind(locAdder)
server.listen(5)

inputs = [server, sys.stdin]
running = True

while True :
    readable, writeable, exceptional =  select.select(inputs,[],[])
    for sock in readable:

        if sock == server:
            conn,addr = server.accept()
            inputs.append(conn)

        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break

        else:

            data = sock.recv(1024)

            if data:
                sock.send(data)
            else:
                inputs.remove(sock)
                sock.close()

        if not running:
            break

server.colse()



