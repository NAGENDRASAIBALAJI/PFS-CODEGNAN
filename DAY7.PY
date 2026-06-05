'''
DAY -7 OF MY PYTHON PROGRAM: OPPS CON
-------------------------
1.CLASS:
--> a class is a blueprint or a template used to create object

2.OBJECT:
-->obj is an instance of a class

---
EG:1
----
class stu_:
    def edu_(self):
        print("i am studing b.tech")


    def sports_(self):
        print("cricket")
        print("vollyball")

s1 = stu_()
s1.edu_()
s1.sports_()
--------------------------------
3.ATTRIBUTES:
--> Attributes are the variables that belongs to a class or an object
----
eg:1
-----
class stu_:
    name = "nani"
    age = 22
s1 = stu_()
print(s1.name)
print(s1.age)



METHODS:
--------

class PFS_DA:
    def PYTHON(self):
        PFS_DA = 'BATCH_03'
        print('This PFS and DA batch03')
    def Flask(self):
        PFS = 'Batch_03'
        print('This PFS batch_03')
all_ = PFS_DA()
all_.PYTHON()
all_.Flask()



CONSTRUCTER:
-->A constructer is a special method that is autoatically called when an object is created
---------------
class ATM:
    def __init__(self,balance, name):
        self.balance = balance
        self.name = name
    def bal_check(self):
        print("f(self.name) your total balance is (self.balance+ 700)")
    def name_(self):
        print(self.name)

card = ATM(balance = 50000, name='Nani')
card.bal_check()
card.name_()


ACCESS SPECIFIERS
-----------------
1.PUBLIC:
-->This can be accessed from anywhere in the program
eg
---
2.PROTECTED:
-->this is represented using a single underscore(_)

3.PRIVATE
-->THIS is represented using a double underscore(__)
EG:
---
class stu:
    __name = 'nani'
s1 = stu()
print(s1._stu__name)

ENCAPSULATION
-------------

--Is the process of binding data and methods together
'''
class bank:
    def __init__(self, balance):
        self.__balance = balance

    def depo_(self, amount):
        self.__balance += amount

    def get_bala(self):
        return self.__balance
acc = bank(1000)
acc.depo_(10000)
print(acc.get_bala())



        

































        
              












