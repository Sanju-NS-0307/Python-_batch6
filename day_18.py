'''
lambda function
---------------
-->lambda function is small anonymous function
-->lambda can take n number arguments ,but only with one expression
-->the function is defined by using lambda keyword.
syntax-->lambda arguments:expression


add=lambda a,b,c:a+b+c
print(add(10,20,30))

even=lambda num:num%2==0
print(even(7))

great=lambda a,b:a if a>b else b
print(great(100,20))


cube=lambda a:a**3
print(cube(int(input())))

filter()
-------
-->filter() function will perform only on selected elements of iterables
syntax:
variable_name=filter(lambda arguments:condition,iterables)
print(datatype(variable_name))

eg:
nums=[1,2,3,4]
data=filter(lambda a:a%2==0,nums)#it will filter elements only when elements meet condition  in iterables.
print(tuple(data))              #

map()
-----
-->map() function will perform on all elements of a iterable.  
syntax-->map(lambda arguments:expression,iterable)
eg:
nums=[1,2,3,4,5]
get=map(lambda a:a+6,nums)# it will perform condition on every element in the iterable.
print(list(get))

reduce()
--------
-->the reduce() function repeatedly applies a function to the elements and reduces them to one final value
-->it is available in the functools module.
syntax-->reduce(lambda arguments:expression,iterable)
eg:
from functools import reduce
data=reduce(lambda a,b:a+b,range(1,11))
print(data)
'''
