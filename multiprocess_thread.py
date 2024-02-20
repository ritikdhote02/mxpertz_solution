import threading
import time

def hell(self):
        for i in range(3):
            time.sleep(1)
            print("hello")
            

def hi(self):
    for i in range(3):
        time.sleep(1)
        print("Hiii")
        

t1 = threading.Thread(target=hell)
t2 = threading.Thread(target=hi)

t1.start
t2.start

t1.join
t2.join

