#Learn How Two Threads Communicate With Each Others
#Learn About Queue() Method
import threading as th  # Import Threading Module
import time as t        # Import Time Module
import queue as q       #import Queue Module 

class Producer():
    def __init__(self):
        self.qu=q.Queue()
    def produce(self):
        for i in range(1,6):
            print("Produce Items:",i)
            self.qu.put(i)
            t.sleep(1)
class Consumer():
    def __init__(self,pro):
        self.pro=pro
    def consume(self):
        for i in range(1,6):
            print("Consume items:",self.pro.qu.get(i))

p=Producer()
c=Consumer(p)
t1=th.Thread(target=p.produce)
t2=th.Thread(target=c.consume)
t1.start()
t2.start()
