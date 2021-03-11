class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, value):
        self._name = value

    def get_name(self):
        return self._name

    def set_age(self, value):
        self._age = value

    def get_age(self):
        return self._age

class Teacher(Person):
    def __init__(self, n, a, pro):
        #super class -> constructor overriding
        super().__init__(n,a)
        self._pro = pro

    def set_pro(self, pro):
        self._pro = pro

    def get_pro(self):
        return self._pro



t = Teacher("","", "")
t.set_name("Puja")
print(t.get_name())
t.set_age(56)
print(t.get_age())
t.set_pro("Professor")
print("I am a {0}".format(t.get_pro()))

