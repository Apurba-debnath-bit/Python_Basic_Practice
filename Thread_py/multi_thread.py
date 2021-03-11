from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for c in range(5):
            print("Hello")
            sleep(2)
        print()

class Hi(Thread):
    def run(self):
        for c in range(5):
            print("hi")
            sleep(2)
        print()
t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print('bye')