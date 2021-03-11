class A:
    def __init__(self):
        print("__init__ from Class A ")

    def feature1(self):
        print("---Feature1 is working from A---")


class B:
    def __init__(self):
        print("__init__ from Class B ")

    def feature1(self):
        print("---Feature1 is working from B---")

class C(A,B):
    def __init__(self):
        super().__init__()

        print("__init__ from Class C ")

#Preferences:
#First--> C class constructor itself
#Then--> Left to right(A is left and B is to right position here)

c1=C()
c1.feature1()