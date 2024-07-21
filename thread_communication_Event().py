#Learn How Two Threads Communicate With Each Others
#Learn About Event() Method
import threading as th #Import Threading Module
import time as t #Import Time Module
def switch_light():
    t.sleep(3)
    e.set()
    print("Green Light ON\n")
    t.sleep(5)
    print("Red Light is ON")
    e.clear()
def traffic():
    e.wait()
    while e.is_set():
        print("You can Go-----")
        t.sleep(0.5)
    print("Stop!!!!")
e=th.Event()
t1=th.Thread(target=switch_light)
t2=th.Thread(target=traffic)
t1.start()
t2.start()
