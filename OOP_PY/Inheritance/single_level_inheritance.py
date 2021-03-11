class Animal:
    def __init__(self, name,a_type, gender, color):
        self.name = name
        self.a_type = a_type
        self.gender = gender
        self.color = color

    def speak(self, sound_ani):
        self.sound_ani = sound_ani
        print(f"Animal sound: {self.sound_ani}")
        print()

    def display_info(self):
        """Here all info will display to user"""
        print(f"Name: {self.name}")
        print(f"Type: {self.a_type}")
        print(f"Gender: {self.gender}")
        print(f"Color: {self.color}")



class Cat(Animal):
    category = ""

    def __init__(self,category,name,a_type, gender, color):
        super().__init__(name,a_type, gender, color)
        #super when calling constructor doesn't take self as parameter
        self.category = category

    def display_info(self):
        super().display_info()
        print(f"Category: {self.category}")


c1 = Cat("Persian","Mumu","Cat","Male","white-dotted")
c1.display_info()
c1.speak("MeuMeu")

