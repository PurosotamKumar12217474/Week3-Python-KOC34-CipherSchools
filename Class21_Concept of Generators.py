#Generators
#//Eagar loading
def generate_square(n):
    return [i**2 for i in range(1,n)]
for i in generate_square(100):
    print(i)
print("")
#//Eagar loading
#Keyword: yield
def generate_square(n):
    for i in range(1,n):
        yield i**2
for i in generate_square(100):
    print(i)

def generate_square(n):
    for i in range(1,n):
        yield i**2
it= iter(generate_square(10))
print(next(it))

def func():
    print("start")
    yield 1
    print("yield 1")
    yield 2
    print("yield 2")
it=iter(func())
next(it)

from time import sleep
def func():
    print("started")
    yield
    sleep(5)
    print("ended")
print("hello")
it=iter(func())
next(it)
print("world")

def generate_square(n):
    for i in range(1,n):
        yield i**2
a=generate_square(10)
print(type(a))

a=(i**2 for i in range(10))
for i in a:
    print(i)
print(type(a))

a=generate_square(10)
print(next(a))

a=(i**2 for i in range(10))
print(iter(a))
print(next(a))
print(next(a))
for i in a:
    print(i)