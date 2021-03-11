class Person:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is: {self.name}")
        print(f"My age is: {self.age}")


class Teacher(Person):

    designation = ""

    def __init__(self,designation, name, age):
        super().__init__(name, age)
        self.designation= designation

    def display(self):
        super().display()
        print(f"I am a  {self.designation}\n")


class Student(Teacher):

    def __init__(self, designation, name, age):
        super().__init__(designation, name, age)
        self.designation = designation

    def display(self):
        super().display()


t1 = Teacher("Teacher", "Apurba", 34)
t1.display()
s1 = Student("Student","Apu",32)
s1.display()


