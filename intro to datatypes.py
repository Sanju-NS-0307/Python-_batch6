'''
Datatypes &typecoversions
-------------------------
1.numaric datatype
------------------
-->Float and interger is called as numaric datatype


float
-----
->A number which contains decimal values , we call it as a float datatype.
eg:
price=56.89

integer(int)
------------
-->A normal values without any decimal values
eg:
num=69
num_2=6


2.String-
--------
-->String is a sequence of characters that are enclosed in '',"","""
-->String is a immutable
eg:
any_='python is a language'
all_='Ab,.&[)-+'

3.list
------
-->list is a collection of different datatypes
-->and it is represented by [] that are separeted by ,
-->inside the list we call it as items
-->list is a mutable
eg:
--
any_=[1,'python',[5,6]]
print(type(any_))


4.tuple
-------
-->tuple is a collection of different data types that are enclosed in () and seperated by ,
-->tuple is immutable
eg:
nums=(1,89.6,'python'[3,4],(8,9))

5.dictionary
------------
-->dictionary is a collection of key:value pairs,key and values are seperated by :
-->key and value pair is call it as a item
--> and this items are seperated by ,
-->dictionary is represented using {}
-->in key place we can use immutable datatypes
-->in values place we can use any datatype
eg:
data_={1:2,'name':'teja',(2,3):'tuple'}
print(data_)


6.set
-----
-->set is a collection of unique elements and set can't allow any duplicate values inside it ...
-->set is represented by {} and the elements are seperated by ,

eg:
an={1,2,3}
print(an)


typeconversion
--------------
float-->int,str
eg:
price=75.98
print(int(price))

-->str()
price=45.78
con=str(price)
print(type(con))

integer --> float,str
->float
eg:
price=45
con=float(price)
print(type(con))

->str()
price=45
con=str(price)
print(type(con))


string--int,float
eg:
do='3456'
print(int(do))

-->float()
do='10.89'
print(float(do))


list-->tuple, str
eg-->tuple
nums=[1,2,3,4,5]
print(tuple(nums))

-->str()

tuple-->list
eg:-->list
all_=(5,6,7)
print(list(all_))


set-->tuple,list
eg:
all_={5,6,7}
print(tuple(all_))

all_={5,6,7,7}
print(list(all_))
print(type(all_))



'''
details=[('name','teja'),('edu','btech')]
print(dict(details))
print(type(details))
