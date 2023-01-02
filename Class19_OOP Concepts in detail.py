a=5
print(isinstance(a,object))
print(type(int))
print(isinstance(a,int))
print("")

class A:
    pass
print(A)

def func():
    pass
print(type(func))

print(isinstance(func,object))

class A:
    name="Jatin"
    marks=50
print(type(A))
A=5
print(type(A))
print(type(int))
print(type(object))
print("")

class A:
    def __call__(self):
        print("You called me")
a=A()
print(a)
print(type(a))
print(a())
print("")

A.__call__(A)

class A:
    pass
b=A.__call__()
a=A()

def func():
    print("Hello")
func.__call__()
print("")

a={"name":"Jatin"}
print(a["name"])
print(a.__getitem__("name"))
print("")

class Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self, x):
        return x**self.n
e=Exponent(2)
e[2]

class A:
    name="Jatin"
    def __init__(self,n):
        self.n=n
a=A(2)
print(a.name)

class Dog:
    kind="canine"
    def __init__(self, name):
        self.name=name

a=Dog("Max")
print(a.name)
print(a.kind)

class Dog:
    trick=[]
    def __init__(self, name):
        self.name=name
    def add__trick(self,trick):
        self.trick.append(trick)

d1=Dog("Max")
d1.add__trick("fetch")
d1.add__trick("talk")
print(d1.trick)

d2=Dog("Bella")
print(d2.trick)
