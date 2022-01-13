class Test:
    a=10
    def __init__(self):
        Test.a=20

    def method(self):
        Test.a=30

    @classmethod  ##decorator
    def method1(cls):   ## class method
        cls.a=40
        Test.a=50

t=Test()
t.method()
t.method1()
print(Test.a)
