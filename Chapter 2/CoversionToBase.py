
#Conversion to expansion base b

a = int(input('Enter base number: '))
b = int(input('Enter decimal number: '))

x=b

while x > 0: 
    print(x%a)
    x = x // a

