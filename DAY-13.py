'''
project based on RegEx:
-----------------------
validation
----------

1.mobile number
---------------
-->10 digits init...


2.password
----------
-->cap,small,digit,special char,atleast 8

3.mail
------

-->@gmail.com
'


import re
class validation_:
    def mob_num(self,num):
        mob = input("enter the 10 digit mobile number:")


import re
mobile_=input("enter the 10 digit mobile number: ")
if re.fullmatch(r'^[6-9)[0-9]{9}',mobile_):
    print("Valid")
else:
    print("Invalid")


'''

import re
name = input("enter name: ")
email = input("enter email: ")
mobile = input("enter mobile number: ")
password = input("enter password: ")

if re.fullmatch(r'^[A-Za-z ]{3,}$',name):
    print("Valid name")
else:
    print("Invalid name")

#email validation
if re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$',email):
    print("Valid email")
else:
    print("Invalid email")

#mobile validation

if re.fullmatch(r'^[6-9][0-9]{9}$',mobile):
    print("Valid mobile number")
else:
    print("inValid mobile number")

#pssword

if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',password):
    print("strong password")
else:
    print("weak password")
    

















































    
