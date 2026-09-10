'''
word=str(input())
rev=''#empty string
for i in word:
    rev=i+rev
    print(rev)
if word == rev:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")


amstrong number 
num=int(input())
length=len(str(num))#need to be conveted into str for iteration through it
amstrong=0
for i in str(num):                   #convert num to str for iterating with 'for' loop and inside loop
    amstrong=amstrong+int(i)**length  add variable to int(i)**length and check for amstrong number.
    print(amstrong)
if amstrong == num:
    print(f'{num} is a amstrong number')
else :
    print(f'{num} is not amstrong number')


num=int(input())
sum=0
for i in range(1,num):    #first find the factors for num and add each factor to variable
    if num%i==0:       and after loop ends ,check num = sum , if same it is perfect number.
        sum+=i
print(sum)
if sum==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is a perfect number')


fibonacci series

num=0
num2=1
print(num,num2,end=' ')
for i in range(1,10):  #the logic is sum of two previous nums is next number and print series 
    num3=num+num2
    num=num2
    num2=num3
    print(num3,end=' ')
'''



