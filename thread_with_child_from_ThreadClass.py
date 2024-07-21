from threading import* #import threading Module
class MyThread(Thread):
    def __init__(self,a,b): #Constructor of Simple Class
        Thread.__init__(self) #Constructor of Thread Class
        print("Sum of Two Numbers=",a+b)
    def run(self):
        print("This is Thread Method")
        
a=MyThread(10,20) #Calling Thread Child Class
a.start()
print("Before=",a.getName()) #Current Thread Name
a.name="Class Thread"
print("After=",a.name)
print("Before Set the Thread Name=",current_thread().getName()) #Current Thread Name
current_thread().setName("This is Main Thread") #Set the Thread Name
print("After Set the Thread Name=",current_thread().getName()) #Current Thread Name
a.run()