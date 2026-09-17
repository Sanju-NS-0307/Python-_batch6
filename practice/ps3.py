#simple scenrio to understand the exception
#a,b=map(int,input('enter the values').split(','))
try:
    a,b=map(int,input('enter the values').split(','))
    result=a/b
    print(result)
except Exception as e:
    print('find it')
    print(e)

#in above case we will get ValueError,ZeroDivisionError
#Possible types of errors-->TypeError,ValueError,NameError,
#IndexError,ZeroDivisionError,AttributeError,ArithmeticError..

try:
    a,b=map(int,input('enter the values').split(','))
    result=a/b
    print(result)
except ValueError:
    print('Bossu sarigaa chusi enter cheyu only integers')
except ZeroDivisionError:
    print('Make sure to give denominator greater than zero')
except NameError:
    print('please first understand the syntax and be good at spellings')
finally :
    print('its done now you have understood exception handling')

#Multiple exceptions at a time
try:
    a=[12,3,4,5]
    print(a[5])#take one example as print(a[45])
    a.append('codegnan')#take one example as a.apend('codegnan')
    print(a)#take one example as print(v)
except (IndexError,NameError,AttributeError) as e:
    print(e)
finally:
    print('done')

'''
try:
    marks=int(input("Enter marks: "))
    if marks>=0 and marks<100:
        if marks>=90:
            print('Grade:A')
            print('Remark:Outstanding!')
        elif marks>=80:
            print('Grade:B')
            print('Remark:Excellent!')
        elif marks>=70:
            print('Grade:C')
            print('Remark:Good!')
        elif marks>=60:
            print('Grade:D ')
            print('Remark:Fair ,needs improvement')
        elif marks>=50:
            print('Grade:E')
            print('Remark:Poor,needs serious improvement')
        else:
            print('Grade:Fail')
            print('Remark:Failed,needs to re-appear')
    else:
        print('Invalid marks entered')
except ValueError:
    print('Invalid marks entered')
    
'''
try:
    number=int(input("Enter a number: "))

    if number==0:
        print("Zero is neither even nor odd")
    elif number<0:
        if number%2==0:
            print("Negative Even Number")
        else:
            print("Negative Odd Number")
    elif number>0:
        if number%2==0:
            print("Even Number")
        else:
            print("Odd Number")
except ValueError:
    print("Enter only Integers")

try:
    month=int(input("Enter month number: "))

    if month==12 or month==1 or month==2:
        print("Season: Winter")
    elif month==3 or month==4 or month==5:
        print("Season: Spring")
    elif month==6 or month==7 or month==8:
        print("Season: Summer")
    elif month==9 or month==10 or month==11:
        print("Season: Autumn")
    else:
        print("Invalid month entered")
except ValueError:
    print("Enter the  valid number")
    '''

