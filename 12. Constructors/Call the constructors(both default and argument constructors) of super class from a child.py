class Parent(object):
    
    def func(self):
        print("Hi, my age is {self.age}!")
    def __init__(self, age):
        self.age = age

class Child(Parent):
    def __init__(self, age):
        super().__init__(age)

dad = Parent(36)
kid = Child(8)

dad.func()
kid.func()
