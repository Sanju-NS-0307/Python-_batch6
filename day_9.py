'''
set operations



union()
------
-->the union() will combine two set into single set
->we can also use " | " for union
syntax-->set_1.union(set_2) or set_1|set_2
eg:
data_={1,2,3,4}
nums={5,6}
print(data_.union(nums))
print(data_|nums)

intersection()
--------------
-->this will gives us the common elements from the both sets
syntax-->set_1.intersection(set_2) and set_1&set_2
eg:
data_={1,2,3,4}
nums={4,5,6}
print(data_.instersection(nums))
print(data_&nums)

difference()
-----------
-->it will display the different elements from set_1, but not the set_2 elements
syntax-->set_1.difference(set_2)
eg:
data_={1,2,3,4}
nums={4,5,6}
print(data_.difference(nums))
print(data_ -nums)
print(nums-data_)

symmetric difference()
----------------------
--> different elements from the both
syntax-->set_1.symmetric difference(set_2)
eg:
data_={1,2,3,4}
nums={4,5,6}
print(data_.symmetric_difference(nums))

operations are completed and next is methods
methods-
-------
add()
-----
-->add() method will add only one element at a time
syntax-->set.add(element)
eg:
data_={1,2,3,4}
print(data_)
data_.add(7)
print(data_)

update()
--------
-->we can add more one elements by using update method
syntax-->set.update([elements]) or set_1.update(set_2)
eg:
data_={1,2,3,4}
nums={4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)

remov()
------
-->remove() method will del the given element from the set
-->if the element is not present in the set , it will raise error
syntax:set.remove(element)
eg:
data_={1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)

discard()
---------
-->the method is used to del the elements fromm the set, but never raise any error even the element
is not inside set
syntax-->set.discard(element)
eg:
data_={1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)

clear()
------
-->the method is used to del all the elements from the set and it will written empty set
syntax-->set.clear()
eg:
data_={1,2,3,4}
print(data_)
data_.clear()
print(data_)
'''

