'''
INHERITANCE:
-----------
-->THis is allows one class to aquire the properties and methods of another class...
types
-----
1.SINGLE INHERITANCE
--------------------
-->A CLASS inherts from a single parent class
1.SINGLE INHERITANCE:
-------------------
class father:
    def land(self):
        print("my father have 5ace")
class nani(father):
    def my_own(self):
        print('i have 2ace')

fam = nani()
fam.land()
-----------------

2.MULTIPLE INHERITANCE:
-----------------------

class father:
    def land(self):
        print("my father have 5ace")

class mother:
    def gold(self):
        print("my mother have 1kg g")

class son(father,mother):
    def my_own(self):
        print('i have 2ace')

all_ = son()
all_.land()
all_.gold()
-----------------------------

3.MULTI - LEVEL INHERITANCE:
----------------------------
   
class grandfather:
    def land(self):
        print("my grandfather have 5ace")

class father(grandfather):
    def flat(self):
        print("have flate at BNG")

class son(father):
    def ntg(self):
        print('i own both of their p')

all_ = son()
all_.land()
all_.flat()
all_.ntg()

--------------------------
4.HIERARCHICAL INHERITANCE:
---------------------------
-->multiple child classes inherts from a simple parent....


class father:
    def land(self):
        print("my father have 10 ace")

class nani(father):
    def min(self):
        print("have a JOB")

class sonu(father):
    def bro(self):
        print('jobless')
son = sonu()
son.land()

so = nani()
so.land()

--------------------
5.HYBRID INHERITANCE:
---------------------
-->THIS IS COMBINATION OF TWO OR MORE TYPE OF INHERITANCE




class c(a):
    def so(self):
        print("class c")

class d(b,c):
    def all_(self):
        print("class d")


how = d()
how.so()

--------------------------------------

** SUPER ()METHOD:
-------------------
-->super() is used to acess methods and constructor of the parent class from the child class


class parent:
    def display(self):
        print("method parent")

class child(parent):
    def display(self):
        super().display()
        print("method child")


any_ = child()
any_.display()

-----------------------

class person:
    def __init__(self,name):
        self.name = name

class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"name : {self.name}")
        print(f"roll no : {self.roll}")

any_ = stu_('nani',103)
any_.show()


-----------------------
POLYMORPHISM:
-------------

-->THIS MEANS 'MANY FORMS'... IT ALLOWS THE SAME FUNCTION,METHOD, OR OPERATOR TO BEHAVE
DIFFERENTLY ON THE OBJECT...

1.METHOD OVERLOADING:
---------------------
-->METHOD OVERLOADING MEANS DEFINING MULTIPLE METHODS WITH THE SAME NAME BUT DIFFERENT PARAMETERS
-------------------
EG:
----
class calcu_:
    def add (self, a, b, c=0):
        return a+b+c
    def sum(self, a, b, c=0):
        return a-b-c

an = calcu_()
print(an.add(23,6))
print(an.sum(23,6,9))



2.METHOD OVERRIDING:
--------------------
-->THIS OCCURS WHEN A CHILD CLASS PROVIDES ITS OWN IMPLEMENTASTION OF A METHOD OVERRIDING
DEFINED IN THE PARENT CLASS...
---------------------
EG:
class animal:
    def sound(self):
        print("Animal Makes Sound")
class dog(animal):
    def sound(self):
        print("dog darks")
ntg = dog()
ntg.sound()

-----------------------
3.OPERATOR OVERRLOADING:
------------------------
-->THIS ALLOWS OPERATORS SUCH AS +,-,*ETC,,, TO PERFORM DIFFERENT ACTIONS FOR
USER-DEFINED OBJECTS

NOTE:
--------
-->THE OPERATOR INSIDE THE METHOD WILL OVERLOAD A SPECIAL METHOD OR OPERATOR
GIVE IN THE CALLING FUNCTION 
----------------  
EG:

class stu_:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, b):
        return self.marks + b.marks
        
so_1 = stu_(4)
so = stu_(78)
print(so_1 + so)
---------------------------
DATA ABSTRACTION:
--> THIS IS THE PROCESS OF HIDING INTERNAL IMPLEMENTATON DETAILS AND SHOWING ONLY ESSENTIAL FEATURES TO THE USER
--> IT FOCUSES ON WHAT AN OBJ DOES FATHER THAN HOW IT DOESIT...
 from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass

class Rec(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 2*(self.a * self.b)

an = Rec(10, 5)
print(an.area())


'''






































































    
















  




















