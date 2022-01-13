class Test:
    a=10
    def __init__(self):
        Test.a=20

    def method(self):    ## instance method
          Test.a=30 

t=Test()
t.method()
print(Test.a)
