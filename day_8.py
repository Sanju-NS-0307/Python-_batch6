'''
tuple
-----
-->tuple is collection of different datatypes that separated by, and represented by ()
-->it is immutable
-->we can pass a tuple of values and that can be asign to the variables,but should match same number
variables and values inside the tuple
eg:
--
t=(1,'python',[3,4],(7,9))

indexing
eg
--
t=(1,'python',[3,4],(7,9))
print(t[2][1])

index()
------
-->if the item is not present in the tuple,it will raise valueError
eg
--
t=(1,'python',[3,4],(7,9))
print(t.index('Python')

len()
----
-->
t=(1,'python',[3,4],(7,9))
print(len(t))

eg:
name, age,batch=('sanjay',21,6)
print(name)
print(age)
print(batch)

max()
---
-->used to find out the maximum value from the tuple
eg:
so=(67,5,89,45)
print(max(so))

min()
----
-->used to find out the minmum value from the tuple
eg:
so=(67,5,89,45)
print(min(so))

count()
-------
-->used to count an item present in the tuple
eg:
so=(67,5,89,5)
print(so.count(5))
'''
so=(67,5,89,45)
do=(45,89)
print(so+do)

