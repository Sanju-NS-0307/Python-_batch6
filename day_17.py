'''
scope of variables

1.local variable
----------------
-->a variable is define inside the function call it as local variable,where the
variable can only access with in that function

eg:
def display():
    name='teja'
    print(name)
display()

2.global variable
-----------------
-->a variable that is defined outside the function call and it can be access anywhere through
out program.
eg:
a=90# if a is declared outside function,by default it is global variable
print(a)
def display(): # if a is declared inside function,we are telling the function that there is
    global a   # access the gloabal varible inside a function.

    a=10
    
display()

print(a)

3.global keyword
----------------
-->global is keyword used to reaccess new values to variables that was already define outside
the function call

a=90
print(a)
def display(): 
    global a   
    a=10
display()
print(a)

passing by variable
eg:
num=10
def even_odd(num):
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)


passing by value
eg:

def even_odd(num):
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)




Recursive function
------------------
-->the function call itself until the base condition met..
'''
def fac(a):
    if a==0 or a==1:
        return a
    return a*fac(a-1)
print(fac(int(input())))

