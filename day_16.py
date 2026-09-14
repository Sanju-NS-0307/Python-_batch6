'''
Functions
---------
-->A function is a block of code that can be exceuted only when it is called..
-->a function start with def keyword and the line called as definition line,where we can define
a function name.
-->and if we want to execute the program in the function,need to call with the function name
define at def line. 

syntax
------
def fun_name(parameters):
    pass
fun_name(arguments)
eg:
def add_(a,b):
    print(a+b)
add_(11,12)

Arguments
---------
postional arguments
-------------------
-->the arguments should be same at def line and calling , incase if they are not same number will
raise an error.
eg:
num=0
num2=1
def fib(num,num2):
    
    print(num,num2,end=' ')
    for i in range(1,10):   
        num3=num+num2
        num=num2
        num2=num3
        print(num3,end=' ')
fib(num,num2)

default arguments
-----------------
--> the default arguments where the function will only consider the data at calling function
,even though data present at def line

eg:
def feb(a,b):
    print(a+b)
feb([1,2,3],[4,5,6])
2.
def data_(a=8,b=9):
    print(a+b)
data_(1,2)

eg:
a=int(input('enter the number'))

def prime(a):
    
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count +=1
            print(count)
    if count==2:
        print(f'{a} is a prime')
    else:
        print(f'{a} is not a prime')
prime(a)

-->keyword arguments
-------
keyword argumenys are the arguments that are passed to the function in the form of key=value pairs. the
order of the arguments is not necessary while calling the function.

eg:
def data(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data(name='teja',age=45,location='vizag',batch='6')

Variable length argument
------------------------
-->Adding a (* call it as args) before a variable at parameters that we can pass tuple of arguments
and can be access with indexing
eg:
def all(*name):
    print(name)
all('teja','sanjay','sunny','vishal')

keyword length arguments
------------------------
-->adding a(** call it as args) before a varible at parameters that we can pass as dictionary
and in the form of key value pairs and it can accessed with dictionary methods.
eg:
def details(**data_):
    print(data_.keys())
details(name='teja',age=45,location='vizag',batch=6)


return
------
-->return keyword used inside the function , once the return is exceuted means it will get back to
calling with return values.
eg:
def all(a,b):
    return a-b
print(all(7,9))
'''
    
