#Learn How We Check the name of Current Thread in Program
import threading #Import threading module
print("In this Program we check the name of Current Thread")
a=threading.current_thread().getName() 
print("Give the Name of Current Thread:",a) #Give the name of Current Thread that is MainThread
