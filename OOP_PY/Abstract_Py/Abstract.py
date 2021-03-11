from abc import ABC, abstractmethod
class Abs(ABC):
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
    @staticmethod
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Section: {self.section}")
        print()


class B(Abs):

    cl =""
    def __init__(self,name, age, cl, section):
        #super(B, self).__init__(name, age,section)
        super().__init__(name, age, section)
        self.cl = cl
    def walk(self):
        print("I can walk...")

    def sleep(self):
        print("I can sleep")

    def display(self):
        super().display(self)
        print(f"Class: {self.cl}")


b1 = B("Apurba", 23,"Nine", "A")
B.display(b1)
b1.walk()
b1.sleep()