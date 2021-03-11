class Person:
    name = ""
    age = ""
    height =""
    weight =""
    gender =""
    phone = ""
    address =""

    def __init__(self, name, age, gender, height, weight, phone, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.phone = phone
        self.address = address


    def display_info(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")
        print(f"I am  {self.gender}.")
        print(f"My height  {self.height}.")
        print(f"My weight  {self.weight}.")
        print(f"My phone no. is  {self.phone}.")
        print(f"My address is  {self.address}.")
        self.talk()
        self.walk()
        print()

    def talk(self):
        print("I can talk")
    def walk(self):
        print("yes! I can walk")

class Teacher(Person):
    designation = ""
    def __init__(self,designation,name, age, gender, height, weight, phone, address):
        super().__init__(name, age, gender, height, weight, phone, address)
        self.designation = designation


t1 = Teacher("Teacher","Apurba",34,"Male",5.6,67,"05677545667","kolabagan/Dhaka")
t1.display_info()

t2 = Teacher("Teacher", "Partho Debnath",45,"Male",5.6,76,"01745431563","Dhaka/Dhanmondi")
t2.display_info()
t2.walk()
t2.talk()




