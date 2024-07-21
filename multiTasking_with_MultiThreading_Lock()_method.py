#Learn MultiTasking With MultiThreading
#Concept of Race Condition
#Learn Thread Synchronization
#Learn How we use Lock() for Thread Synchronization
import threading as a #Import Threading Module
class Bus:
    def __init__(self,total_seats):
        self.total_seats=total_seats
        self.lock=a.Lock()
        #print("Befor Acquire:",self.lock)
    def buyseats(self,need_seats):
        self.lock.acquire(blocking=True,timeout=-1)
        #print("After Acquire",self.lock)
        print("Total Free Seats=",self.total_seats)
        if(self.total_seats>=need_seats):
            customername=a.current_thread().name
            print(need_seats,"Seats are alloted For",customername)
            self.total_seats =self.total_seats-need_seats
            print("Reamining Seats:",self.total_seats)
        else:
            print("Sorry!All Seats are Full")
        self.lock.release()
        #print("After Release",self.lock)

b=Bus(3)
t1=a.Thread(target=b.buyseats,args=(2,),name="Abdul Khaliq")
t2=a.Thread(target=b.buyseats,args=(1,),name="Ali")
t3=a.Thread(target=b.buyseats,args=(1,),name="Waleed")
t4=a.Thread(target=b.buyseats,args=(2,),name="Akram")
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("END Program")
