#Learn How Two Threads Communicate With Each Others
#Learn About Condition() Method
import threading as th  # Import Threading Module
import time as t        # Import Time Module

lst = []

def produce():
    c.acquire()
    #c.notify()  # Notify after producing all items
    for i in range(1, 6):
        lst.append(i)
        t.sleep(1)
        print("Generate Item")
    c.notify()  # Notify after producing all items
    #c.notify_all() This can be used when you want to call more than one Function
    c.release()

def show1():
    c.acquire()
    c.wait(timeout=0)
    print(lst)
    print("Program End")
    c.release()
    #print(lst)
    #print("Program End")

c = th.Condition()
t1 = th.Thread(target=produce)
t2 = th.Thread(target=show1)
t1.start()
t2.start()