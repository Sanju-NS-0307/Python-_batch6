'''
bit wise operators

&--> and operator
5--0101
3--0011
1--0001
print(5&3)

|-->or operator
5--0101
3--0011
7--0111
print(5|3)

^-->bitwise xor
5--0101
3--0011# same values false and different true
6--0110
print(5^3)

>> --> right shift
5-->0101
1-->0001
0001
print(5>>2)

<< -->left shift
5-->00101--10100#print(5<<2)
10-->1010
print(5<<1)


input formatting
----------------

integer-->int(input())
b=int(input("enter any number: "))


float-->float(input())
b=float(input("enter any decimal: "))

string--> can give directly without mentioning datatype
so=input("enter a string")
print(type(so))

list-->
names=list(map(str,input("enter names:").split()))
print(names)

tuple-->
nums=tuple(map(int,input("enter numbers:").split()))
print(nums)

**eval--> should follow particular datatype rules
data_=eval(input('enter:'))
print(type(data_))    -->can be used for any datatypes according to its rules

-->output formatting
name='sanjay'
age=67

print('my name is',name,'age is',age)
print('hello',name)

print(f'my name is {name} and i am {age} years old') #fstring

%
name='sanjay'
age=67

print('my name is %s and i am %d years old'%(name,age))
'''

