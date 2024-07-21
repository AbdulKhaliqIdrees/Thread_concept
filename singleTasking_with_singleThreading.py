#Learn How We Use Single Tasking With Single Threading
import threading as a #Import Thredaing Module
import time as b #Import Time Module
class QuestionPaper:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def solution(self):
        self.ques1()
        b.sleep(3)
        self.ques2()
        b.sleep(3)
        self.ques3()
        b.sleep(3)
    def ques1(self):
        print("Solve Question:1",self.a)
    def ques2(self):
        print("Solve Question:2",self.b)
    def ques3(self):
        print("Solve Question:3",self.c)

q=QuestionPaper("Define Hardware","Define CPU","Define Computer")
t=a.Thread(target=q.solution)
t.start()
