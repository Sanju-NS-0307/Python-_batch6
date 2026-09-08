'''
Strings
-------
operations
----------
1.indexing
----------
-->indexing is used to get char that you looking to access
types
1.positive indexing
-------------------
positive indexing starts from 0 index
syntax-->varible_name[index_value]
eg:
text='python'
print(text[3])

2.negative indexing
-------------------
negative indexing starts from -1 index
syntax-->print(variable_name[negative index_postion]
eg:
text='python'
print(text[-1])

len()
----
-->len() is a built-in function that is used get number of char present in the string
syntax-->len(variable_name)
eg:
txt ='python is a programming language'
print(len(txt))

slicing
-------
-->this is used to access the particular part from the string
syntax-->variable_name[start:end]
eg:
txt ='python is a programming language'
print(txt[12:])
print(txt[:23])
print(txt[12:23])

txt ='python is a programming language'
print(txt[::-1])   #palindrome built in function

txt ='madam'
print(txt[::-1])

upper()
------
-->used to convert all small char into capital
eg:
txt ='python is a programming language '
print(txt.upper())

lower()
------
-->used to convert all cap into small
eg:
txt ='PYTHON'
print(txt.lower())

index()
------
-->used to know the index postion of an char
syntax-->variable_name.index('substring',start,end)
eg:
txt ='python is a programming language '
print(txt.index('i'))

txt ='python is a programming language '
print(txt.index('i',9,18))

repalce()
--------
-->used to replace old substring
syntax-->variable_name.replace('old','new')
eg:
txt ='python is a programming language '
print(txt.replace('python','java'))

split()
-------
-->this method is used to separate string based on the given sub string.output will be given in list form.
syntax-->variable_name.split(substring)
eg:
txt ='python is a programming language '
print(txt.split(' '))

count()
-------
-->used to count number of occurences of an sub string
syntax-->variable_name.count('substring',start,end) #start and end are not mandatory


'''
txt ='python is a programming language '
print(txt.split('o'))
