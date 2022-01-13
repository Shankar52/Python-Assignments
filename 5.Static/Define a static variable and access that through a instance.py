class Test:
    a=10
    def  __init__(self):
        print(self.a)
        print(Test.a)

    def method(self):   ##accessing the static variable inside the instance method
        print(self.a)    ## by using self variable
        print(Test.a)    ## by using classname

t=Test()
t.method()                ##calling instance method
