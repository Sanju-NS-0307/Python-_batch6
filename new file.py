'''
tokens
-----
-->Tokens are the small unit in the python..

1.identifiers
------------
--->identifier is a name of variable or function or class


-->variable
eg:
num='python'
print(type(num))

-->functions
eg:
def add_(a,b):
    print(a+b)

add_(4,5)


-->class
eg:
class details:
    pass

per_1=details


2.keywords
----------
--->Keywords are already saved in python for an specified reason to run..
eg:
if
else
for
while
return
print


3.literals
----------
--->literals are the data types that need to be stored in varibles ...
eg:
num=69
name='sanjay'

4.operator
-----------
+,-,=,


statements
----------
--->statements are the instructions given to the program...

num=90
age=2
if age>=18:
   print(age)


comments
--------
-->once comments are open the lines inside will never execute in python file
1.single line(#)
--->used to comment only one line
eg:
age=20
if age>=18: #this check age is greater or equal
   print(age)

   
2.multi-line(''' ''',""" """)
-----------------------------
-->used to comment more than one line

variables rules
---------------
Bad ways
--------
1.can't  use number at 1st postion
2.cannot use special charcater anywhere
3.cannot use space
4.should not use keywords

eg:
2num=90 #error
$num=89 #error
n um=78 #error
if=67   #error

good ways
---------
-->small letters and cap letters,(_) underscore

num_1=24
Num_2=78
teja_garikipati=90

a={'name':'teja',
   'AC_num':'445896987645'}
b={'name':'nagamani',
   'AC_num':'445896995645'}
c={'name':'sunny',
   'AC_num':'445896987960'}

sbi_details={'name':'teja',
   'AC_num':'445896987645'}
icici_details={'name':'indumati',
   'AC_num':'445896981221'}

   
num=90
print(num)

num_2,num_3=14,53
print(num_2)
print(num_3)

swaping
a,b=45,67
print('a=',a)
print('b=',b)
a,b=b,a
print('a=',a)
print('b=',b)

'''
a,b=45,67
print('a=',a)
print('b=',b)
a,b=b,a
print('a=',a)
print('b=',b)
