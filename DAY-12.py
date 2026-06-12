
'''

12-DAY OF MY PTHON PROGRAMMING:
-------------------------------

REGULAR EXPRESSION (REGEX):
---------------------------
-->REGULAR EXPRESSION IS A SEQUENCE OF CHAR THAT FROM A SEARCHING PATTERN...
--> THIS CAN BE USED TO CHECK IF A STRING CONTAIN THE SPECIFIED SEARCH PATTERN
-->PYTHON HAS A BULIT-IN PACKAGE CALLED 'RE' WHICH CAN BE USED TO WORK WITH REGEX..



FUNCTIONS IN RE
---------------
1.FIMDALL
2.SEARCH
3.FULLMATCH


MATACHAR:
---------
[]-->a-z,A-Z,0-9 and any specified squence..
.-->here each . is one char
^-->this look for the ,string is starting with specified sequence or not...
$-->this is look for the, string is ending with specified squence or not...
*-->zero or more
?-->zero or one
()-->
---------------------------------
import re
any_ = "c is progAam lang"
print(re.findall('[a]',any_))

--------------------------------
import re
any_ = 'c is a programming lang'
print(re.search('[als]',any_))
--------------------------------
import re
any_ = 'python is a programming lang'
print(re.search('^ pythn is ',any_))
-------------------------------------------
import re
any_ = 'python is a programming lang'
print(re.findall('python$',any_))
-----------------------------------
import re
any_ = 'python is a programming lang'
print(re.findall('p.*thon',any_))
-----------------------------------------
import re
any_ = 'python is a programming lang'
print(re.findall('p.?thon',any_))
------------------------------------
import re
any_ = 'python is a programming lang'
print(re.findall('p.{7}',any_))
------------------------------------
special squence
---------------
\S ---no space
\s--only space
\D-->non-digits
\d-->only digits
\w-->mathcs any word char (letter,digits,underscore)
\W--> non words
-----------------------------------
import re
any_ = 'python is a programming  1326357 lang'
print(re.findall('\d',any_))


------------------------------
find the mobile no:

'''
import re
mobile_ = input("enter 10 digit no: ")
how  = re.fullmatch('[6-9][0-9]{9}',mobile_)
if how:
      print(f"{mobile_} this is india number")
else:
    print(f"{mobile_} this is not india number")
                    































