#Learn How we make Thread without Inheriting Child from Thread  Class Module
import threading as a #Import Threading Module
class Sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,p,q):
        print("Sum of Two Numbers=",self.a+self.b)
        print("Subtraction of Two Numbers=",p-q)

s=Sum(10,22)
t=a.Thread(target=s.add,args=(20,5))
t.start()
