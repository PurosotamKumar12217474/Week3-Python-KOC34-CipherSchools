class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self):
        print("B init executed")
abc=B()

class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init executed")
abc=B()

class SchoolMember:
    '''Represent any school member.'''
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("(Initialized SchoolMember: {})".format(self.name))
    
    def tell(self):
        '''Tell my details.'''
        print('Name:"{}"Age:{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary=salary
        print("(Initialized Teacher: {})".format(self.name))

    def tell(self):
        super().tell()
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represent a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print('(Initialized Student: {})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{id}"'.format(self.marks))

t=Teacher("Mr. Ujjawal", 40, 30000)
s=Student("Nikhil", 25, 75)

class Car:
    def __init__(self, model, mileage):
        self.model=model
        self.mileage=mileage
    def __str__(self):
        return "{} {}".format(self.model, self.mileage)
    def __repr__(self):
        return "{}".format(self.model)
    def __eq__(self,other):
        return self.mileage == other.mileage
    def __add__(self,other):
        return self.mileage + other.mileage
c1= Car('a',2)
c2= Car('b',2)
c1+c2

#MRO(Method Resolution Order)
class A:
    pass
class B(A):
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)

print(E.mro)
print(E.mro())

#Iteration protocol --> For every object to be iterable, it should have 2 dunders(__iter__ and __next__)
a=range(5)
it= a.__iter__()
print(it)
print(it.__next__())
print(next(it))
##Protocol 
# --> object's "__iter__" should return iterator.
# --> iterator's "__next__" should return the new value on every call.
# --> If the iterator reaches the end, it should raise an "stopIteration" exception.

a="Jatin"
print(iter(a))

class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        pass
class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i=0
    def __next__(self):
        ret= self.i
        self.i +=1
        if ret >= self.myrange.n:
            raise StopIteration
        return ret
a=myrange(5)
it=iter(a)
next(it)
