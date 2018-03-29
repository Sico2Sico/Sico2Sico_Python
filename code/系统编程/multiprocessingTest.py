#coding=utf-8
from multiprocessing import Process
import os



def run_prco(name):
    for i in range(10):
        print('子进程运行中，name= %s' % (name))



if __name__ == '__main__':
    print('父进程 %d' % os.getpid())
    p = Process(target=run_prco,args=("test"))

    p.start()
    p.join()
    print("子进程结束")
