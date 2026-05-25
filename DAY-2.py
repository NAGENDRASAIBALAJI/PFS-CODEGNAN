'''
functions
---------------
----> A function is block of code whic olny execute when it is called
---->you can pass data, know as parameters into a function
----> to avoid repeated lines in code


def function_name(parameters):
    ----------------
    ----------------
function_name(arguements)

num = 10
def even(num):
    if num % 2 == 0:
        print(f"{num} even")
    else:
        print(f"{num} odd")
        
    even(num)
    even(109)
    
-----------------------------
way to pass arguments
-----------------------------
1.Required arguments
--->A function must be called with the same parameters
ex :
  num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} even")
    else:
        print(f"{num} odd")
    even(num, 90)
-------------------------------
2. default arguments:
--->by default, values is defined at parameters even the it will take from arguments.


def even(name,age , sal):
    print(name)
    print(age)
    print(sal)
even(name="nani",age=21, sal=80000)
even("nani",21,80000)

--------------------------------
keyword arguments:
--->you can send arguments with key = value syntex, by this , the order of arguments doesn't matter.
ex:
def even(name,age , sal):
    print(name)
    print(age)
    print(sal)
even(name="nani",age=21, sal=80000)
even(name = "nani",age = 21,salary = 80000)
--------------------------------------------------
varible length arguments :
---->adding a star(*) before the parameter name in the function, recieve a tuple of arguments and can aacess items with indexese

ex:
def even(name,age , sal):
    print(name[1])
    

-------------------------------
1. sum of two numbers
def num(a,b):
   print(a+b)
sum(3,4)
-------------------------------
2. checking weather number is even or odd:


 num = int(input())
 def and num():
 if num % 2 == 0:
     print("Even number")
 else:
     print("Odd number")
-----------------------------
''''





























     



























































