from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(7):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(7):
            print("ho")
            sleep(1)

t1=Hello()
t2=hi()
t1.start()
sleep(0.23)
t2.start()
t1.join()
t2.join()
print("bye")
