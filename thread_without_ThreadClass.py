#Learn How we make our own thread without using Thread Class
from threading import* #Import threading module
def sum(): #Make Simple Function//Run under the Thread that we make (Thread-1,Thread-2)
    for i in range(5):
        print("Current Thread Name",current_thread().getName()) #Get the Current Thread Name(Thread-1,Thread-2)
a=Thread(target=sum,name="AK47") #Create Thread-1
b=Thread(target=sum) #Create Thread-2
a.start() #Run Thread-1
a.join()
print(a.name)
print("Current Thread:",current_thread().getName())
b.start() #Run Thread-2
b.join()
print("Current Thread:",current_thread().getName())
for i in range(5): #Run Under Main Thread
    print(i)
print("Current Thread Name:",current_thread().getName()) #Get the Current Thread Name(MainThread)




