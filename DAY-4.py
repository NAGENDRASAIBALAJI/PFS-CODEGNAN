'''
list comprehension:
------------------
-->this list comprehension offers a shortest  syntax when we want to create a new list from existing list

syntax ---> vari_name = [expression loop condition]
----------
old_ = [1,2,3,4,5]
new_ = [so if so%2!=0 else "even" for so in old_]
print(new_)
------------------------
generators:
--> generators in python are a special type of itterable, allowing users to iterate over data efficiently
without storing everything in memory..
-->they genrate values lazily using yield key word


why to use generators
---------------------
---> generators do not store the entire dataset in memory ,they generater values on the fly
---> avoiding the unnecessary storage of data speed up execution.
how it works
-------------
-->it looks like normal function but uses the yield keyword instead of return
-->when the function is called ,it does not execute immediately. instead, it return a generator object which
can be iterated using loop or the next() function

----------------------------
def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

----------------------------
def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))
---------------------------

def sqr(num):
    result = []
    for i in range(1, num+1):
        result.append(i*i)
    return result
print(sqr(5))

def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))

----------------------
'''
so = 'quantum computing is an advanced field of technology that hardnessess the law of quantum'
any = ''
for j in so:
    if j not in "AEIOUaeiou":
        any += j
print(any)














































    
