'''
if statement
------------
-->if condition become true , then it will execute inside block of code
-->incase it becomes false,then it will never enter inside of block
eg:
age=15
if age>=18:
    print('eligible to vote')

print(age)

eg:
age=19
if age>=18:
    print('eligible to vote')

print(age)

eg:
a=90
b=78
if a>b:
   print(a)

if-else
-------
-->else for if statement is a fall back statement ,incase if condition  is false then else block
will execute
eg:
a=90
b=78
if a>b:
   print(a)
else :
    print(b)

num=65
num_2=78
if num>num_2:
   print(num)
else :
    print(num_2)


a=75
if a>60:
   print('eligible for pension')
else :
    print('not eligible for pension')


a=18
if a>=18:
   print('entered adulthood')
else :
    print('in childhood')

interview_score=45
if interview_score>50:
   print('eligible for next round.All the best!')
else :
    print('you did not clear the round.better luck next time')


elif
----
-->elif statement is used to check more possible outcomes or more conditions
eg:
a=90
b=780
c=670
if a>b and a>c:
   print(a)
elif b>a and b>c:
   print(b)
else:
   print(c)


num=7
num_2=3
user_opt=int(input('enter \n1.add \n2.sub \n3.mul \n4.pow:'))
if user_opt==1:
   print(num+num_2)
elif user_opt==2:
   print(num-num_2)
elif user_opt==3:
   print(num*num_2)
else:
   print(num**num_2)
   

nested if
---------
-->if statement inside an if statement are called nested if statements. 
eg:
app_details={'pin':1234}
import random
user_pass=int(input('enter your app password:'))
otp=random.randint(1000,9999)
if user_pass ==app_details['pin']:
   print('passowrd is correct')
   print(otp)
   user_otp=int(input('enter 4 digit otp: '))

   if user_otp==otp:
      print('welcome to the app')
   else:
      print('incorrect otp')
else:
   print('password is incorrect')

eg:
a=int(input('enter a number:'))
if a%2==0:
   print(f'{a} is even')
else:
   print(f'{a} is odd')
'''
marks=int(input('enter your marks:'))
if marks>=90:
   print('A+')
elif marks>=80:
   print('A')
elif marks>=70:
   print('B+')
elif marks>=60:
   print('B')
elif marks>=50:
   print('C+')
elif marks>=40:
   print('C')
else:
   print('D')

   


    
    
