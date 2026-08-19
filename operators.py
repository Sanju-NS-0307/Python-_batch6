'''
concatination
-------------
-->the + will behave two ways for numaric it works normally and for other data types like string ,list,tuple
it will concatinate

num=90
num_2=7
print(num+num_2)
an='python'
of='language'
print(an+of)

operators
---------
-->the operators are used to perform operations in variables and the values..

1.Arthematic operator
---------------------
+,-,*,/,//,%

+ --> to add the values
num=90
num_2=7
print(num+num_2)

'-'
eg:
a=4
b=9
print(b-a)

'*'
v=8
n=4
print(v*n)

'/'
v=18
n=9
print(v/n)

'//'--floor division
v=8.5
n=4.4
print(v//n)

'%' modulo
a=15
b=6
print(a%b) #prints remainder


2.assignment operator
---------------------
=,+=,-=,*=,%=,/=

+= --> is increment operator
a=0
print(a)
a+=1
print(a)

-= --> decrement operator
b=67
b-=5
print(b)

*= -->
a=5
a*=3
print(a)

%=-->
a=5
a%=3
print(a)  #gets remainder

/= -->
a=5
a/=3
print(a) #gets complete division value

//= -->
a=5
a//=3
print(a) #floor division ,gets only integer value


3.comparison operator
---------------------
-->==,>=,<=,>,<

num=9
num_2=5
print(num!=num_2) #9!=5
print(num==num_2) #9==5
print(num>num_2)  #9>5
print(num< num_2) #9<5

4.logical operator
------------------
-->and -all condtions should agree then true
-->or- any condition should agree and then true
-->not - inversion= complete opposite output   
num=9
num_2=13
print(num>=num_2 and num<=10) #9>=13 and 9<=10
print(num<=num_2 and num<=10) #9<=13 and 9<=10

5.identity operator
-------------------
-->
num=45
num_2=45
print(id(num))
print(id(num_2))
print(num is num_2)
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is b)

-->
a=[1,2]
b=[1,2]
print(a==b)
print(a is b)

-->is not
a=[1,2]
b=[1,2]
print(id(a))
print(id(b))
print(a is not b)


6.membership operator
--------------------
-->
in
not in

nums='python is language'
print('y' in nums)
print('i' not in nums)


7.bitwise operator
'''


arithmetic

a=3
b=7
print(a+b)

c=4
d=9
print(d-c)

e=8
f=4
print(e*f)

g=18
h=9
print(g/h)

j=8.5
i=4.4
print(j//i)

k=15
l=6
print(k%l) #prints remainder

-->assignment

+=

m=0
print(m)
m+=1
print(m)

-= 
n=67
n-=5
print(n)

*= 
o=5
o*=3
print(o)

%=
p=5
p%=3
print(p)  #gets remainder

/= 
q=5
q/=3
print(q) #gets complete division value

//= 
r=5
r//=3
print(r) #floor division ,gets only integer value

comparsion

s=9
t=5
print(s!=t) #9!=5
print(s==t) #9==5
print(s>t)  #9>5
print(s< t) #9<5

logical

u=9
v=13
print(u>=v and u<=10) #9>=13 and 9<=10
print(u<=v and u<=10) #9<=13 and 9<=10

identity

-->is

w=[1,2]
x=[1,2]
print(w==x)
print(w is x)

-->is not
y=[1,2]
z=[1,2]
print(id(y))
print(id(z))
print(y is not z)

membership 

in
not in

check='love is divine'
print('v' in check)
print('i' not in check)



























