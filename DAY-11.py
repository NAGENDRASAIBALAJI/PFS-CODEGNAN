'''
DAY--11 OF MY PYTHON

ERROR HANDLING:
---------------
TRY BLOCK:
---> THE TRY BLOCK,TEST A BLOCK OF CODE FOR ERROR

EXCEPT BLOCK:
--> THE EXCEPT BLOCK LET HAND IF THE CODE CONTAIN ERRORS...


ELSE:
-----
-->THIS WILL BE EXCUTED, IF ANY BLOCK HAS NO ERROR IN THE CODE...

FINALLY BLOCK:
--->THIS WILL BE EXCUTED EITHER TRY BLOCK CONTAIN ERROR OR NOT...

--------------------------
EX1:
try:
    print("HAI")

except:
    print('this will handle zerodivisionerror')

else:
    print("no error")
----------------------

try:
    print(a)
    print(5+"HAI")

except typeerror:
    print('this will handle typeerror')
except nameerror:
    print("this will handle nameerror")

else:
    print("no error")

'''

try:
    PRINT("hAI")

except:
    print("error")
else:
    print('no error')
finally:
    print('end')

























    
