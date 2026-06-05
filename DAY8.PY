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


'''

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




















  




















