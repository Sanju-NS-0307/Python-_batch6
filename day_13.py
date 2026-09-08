'''limit=100
total=0
for i in range(2,limit+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count==2:
        total+=1
print(total)
'''
star=int(input("enter the number: "))

for i in range(1,star+1):
    for j in range(i,star+1):
        
        print('*',end=" ")
    print()
