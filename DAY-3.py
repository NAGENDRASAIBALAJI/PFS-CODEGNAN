'''
built-in functions
-------------------
print()
input()
len()
type()
min()
max()


ex:
m = [3,4,1,2,]
m.sort()
print(m)

RECURSIVE FUNCTIONS
--------------------
-->A recursive functions that calls itself to solve a problem by breaking it into
small or simple sub-problems

def fac(num):
    if num == 1:
        return 1
    return num * fac(num -1)
print(fac(5)) 
---------------------------


def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)

--------------------------------
def even(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

even(452677)
return
---------------------------
this ends a function execution and send a value back to the code that called the funtion

ex:
def add(a,b):
    return a+b
res = add(4,5)
print(res)
-------------------------------
'
def add(a, b):
    print(a + b)

add(10, 50)
-----------------------
LAMBDA FUNTION:
----------------------
--->A lambda function is a small anonamus functions

-------
syntax---> lambda arguments  : expression
-------
'
so = lambda a,b,c:a+b+c
print(so(3,4,5))






























 
























  







































































