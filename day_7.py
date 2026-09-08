'''
list
----
-->collection of different data types that are seperated by comas and enclosed by square brackets
syntax-->list_name=[e1,e2,e3...]
eg:[1,'python',[1,2],(1,2,3)]


indexing
--------
positive -->0
negative-->-1

data_=['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])


len()
----
-->the function is used to find the number of items present inside list
eg:
data_=['python',[1,2,(90,'details',[67,0]),(78,'student')]]
print(len(data_))

slicing
-------
-->
data=[1,2,3,4,5,6,7]
print(data[2:6])

a=[1,2]
b=[3,4]
print(a+b)

**except int, all like string , list,tuple can be concatenated.


methods
-------
append()
-------
-->append method will add new items to end of the list
syntax:list_name.append(item)
eg:
go=[1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

extend()
--------
-->extend() will add the items into a list at last indexpostion, but it will give each value as one index
inside list.
syntax:variable_name.extend(items)

*difference between append() and extend() is , append directly adds the item to list and where as extend ,iterates through it.
extend is not possible int because it cant be iterated.
eg:
go=[1,2]
go.extend('python')
print(go)

pop()
----
-->pop() is used to remove items from the list and it will delete based on the index postion
syntax-->variable_name.pop(index_postion)
eg:
---
m=[5,1,2,3,4,'python']
m.pop(5)
print(m)

remove()
-------
-->remove() will delete items based on the value given init..
syntax--> variable_name.remove(value)
eg:
m=[5,1,2,3,4,'python']
m.remove('python')
print(m)
'''

