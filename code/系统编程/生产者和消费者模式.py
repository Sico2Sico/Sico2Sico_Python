#encoding=utf-8
import threading
import time

#python2中
from Queue import Queue

#python3中
# from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global  queuec
        count = 0

        while True:
            if queuec.qsize() < 1000:
                for i  in range(100):
                    count += 1
                    msg = "生产产品"+str(count)
                    queuec.put(msg)
                    print(msg)

            time.sleep(0.5)



class Consumer(threading.Thread):
    def run(self):
        global  queuec
        while True:
            if queuec.qsize() > 100 :
                for i in range(3):
                    msg = self.name + " 消费了"+ queuec.get()
                    print(msg)

            time.sleep(1)




if __name__ == '__main__':

    queuec = Queue()

    for i in range(500):
        queuec.put('初始产品'+str(i))

    for i in range(2):
        p = Producer()
        p.start()


    for i in range(5):
        c = Consumer()
        c.start()