'''
a,b=13,4.5
print(a,b)
print(9,15,sep=',')
print('codegnan','python','vizag',sep='-->')
'''
#end by default throws new line,we can modify it
#print(a,b,end=' ')
#print("codegnan is in vizag",end='\t')
'''
a,b=map(int,input()).split(','))
print(f'addition of two numbers is {a+b}')
print(f'subtraction of two numbers is {a-b}')
print(f'multiplication of two numbers is {a*b}')
print(f'division of two numbers is {a/b}')

#usage of %d,%f,%s
#print("usage of %"%(args))
price=45.3;grade='A';stock=15
#print('%d'%price)
#print('%d'%grade)#type error
#print('price is %d'%price)
#print('price is %d'%price)
#print('price is %d'%price)
#print('price is %d'%price)

r=3.5
area=3.1416*r**2
print("area of circle with radius %.1f is %.2f"%(r,area))
'''
#control block statements --> they control the flow of the program


#BMI
height_format = int(input("Enter height format: 1.ms 2.cms 3.fts \nchoice:"))
if height_format == 1:
    input_ = int(input("Enter height in ms: "))
    height = input_
elif height_format == 2:
    input_ = int(input("Enter height in cms: "))
    height = input_ /100
elif height_format == 3:
    input_ = int(input("Enter height in fts: "))
    height = input_ / 3.281
else:
    print("Invalid input")

weight = int(input("Enter weight in kgs: "))

if height > 0 and weight > 0:
    bmi = weight/(height**2)
    print("BMI = %.1f"%bmi)
    if bmi < 18.5:
        print("UnderWeight")
    elif bmi < 24.9:
        print("Healthy weight")
    elif bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")
else:
    print("Invalid input")

