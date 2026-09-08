'''
dictionary
----------
-->dict is a collection of key:value pair
-->key must be unique and it should be immutable datatype(int,str,tuple)
-->dict is represented in {}

details={1:2,'name':'teja',(1,2):[1,2]}



Accessing
---------
-->dict can access by calling key, we will get value from that key
syntax-->dict['key']

-->get() method is also used to get the value from the that key
syntax-->dict.get(key)
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_['adr'])
print(data_.get(2))

UPDATE()
-------
-->method is used update a key, incase if the key is not present inside dict then it add that key:value
syntax-->dict.update({key:value})

-->there is another way to update a key
syntax-->dict[key]=value
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_)
data_['name']='sony'
print(data_)
data_['city']='vizag'
print(data_)

data_.update({'name':'harika'})
data_.update({'ATMPIN':7899})
print(data_)

values()
-------
-->values() method is used to get all the values from the dict
syntax->dict.values()
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_.values())

key()
----
-->keys() method is used get all the key from the dict
syntax-->dict.keys()
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_.keys())

items()
-------
-->the method will get the key:value seperated from the dict.
syntax-->dict.items()
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_.items())

clear()
------
-->clear() method is used to del all data from dict
syntax-->dict.clear()
del dict[key]-->it is used for deleting particular item
eg:
data_={'name':'teja',
       'balance':7000,
       'adr':15643448347,
       'PANC':'GPXBP2890Y',
       2:[3,4]}
print(data_)
del data_['adr']
print(data_)
data_.clear()
print(data_)
'''
