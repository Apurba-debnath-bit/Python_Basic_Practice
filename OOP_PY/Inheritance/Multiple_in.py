class A:
    name = ""
    age = ""
    gender = ""

    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")



a1 = A("Apurba",23,"Male")
a2 = A("Shuvra",25,"Female")

#Here, a1 , a2 is reference variable
#A() means object creation

#a1.display_info()
#a2.display_info()

class B(A):
    designation = ""

    def __init__(self,name,age,gender,designation):
        super().__init__(name,age,gender)
        self.designation = designation
    def display_info(self):
        super().display_info()
        print(f"Designation: {self.designation}\n")


b1 = B("Ap",45,"Female","Teacher")
b1.display_info()

#This will not work because class B() derived from Class A()
#Here, A and B are nnot seperate class
#For MUltiple inheriatnce < There should be two different class derived by one child class
# class C(A,B):
#     pass
#
#
# c1 = C("Puja",34,"Female","Professor")
# c1.display_info()
