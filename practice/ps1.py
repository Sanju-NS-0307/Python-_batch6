'''
student marks analyzer


marks=[]

for mark in range(3):
    mark=int(input("enter the marks:"))
    marks.append(mark)
#print (marks)
marks.insert(0,90)

marks.extend([75,85])

if 75 in marks:
    marks.remove(75)

print(marks.pop())

print('final list is',marks)

print('length of the list is',len(marks))

numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

num=int(input())
if num in numbers:
    print(numbers.count(number))
    print(numbers.index(number))
else:
    print('number not found')

min(numbers)
max(numbers)
sum(numbers)
'''
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

print(numbers[:3])
print(numbers[:-3])

f=numbers.copy()
numbers.clear()
print(numbers)
print(f)
