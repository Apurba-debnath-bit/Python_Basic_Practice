class Building:
    name = ""
    height = ""
    archi =""
    def __init__(self, name, height,archi):
        self.name = name
        self.height = height
        self.archi = archi
    def display(self):
        print("The Building's name: ",self.name)
        print("The Building's Height: ",self.height)
        print()

    def make(self):
        print(f"-----{self.name} made by {self.archi}. -----")

#here, b1, b2 is reference variable:
#b2 is reference variable:
#Building() means creating object of Building class

b1 = Building("Bilas", 234.5,"Mr. ratan")
b2 = Building("Sova Bilas", 23456.7,"Mr. Apu")

b1.display()
b2.display()

b1.make()
b2.make()

