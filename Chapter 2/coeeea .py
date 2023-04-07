
print("GCD(x,y) = sx + ty")
a = int(input("Enter Number: "))
b = int(input("Enter Number"))
x = a
y = b

x0 = int(0)
x1 = int(1) 
y0 = int(1)
y1 = int(0)

while a != 0:
    (q, a), b = divmod(b, a), a
    y0, y1 = y1, y0 - q * y1
    x0, x1 = x1, x0 - q * x1
   
print("GCD(" + str(x) + "," + str(y) + ")" + "=" + "(" + str(x0) + ")" + str(x) + " + " + "(" + str(y0) + ")" + str(y) )
print(b)
print(x0)
print(y0)   
#return b, x0, y0