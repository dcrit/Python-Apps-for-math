x = int(input("Enter Number: "))
y = int(input("Enter Exponent: "))
n = int(input("Enter Mod: "))

p = 1 
s = x 
r = y 
w = 0
while r > 0:
    w += 1
    print("")
    print("Iteration: " + str(w))
    if (r % 2) == 1: 
        p = p*s % n
        print("Mod = " + str(p))
    s = s*s% n 
    r = r // 2
    print("s OR x = " + str(s))
    print("r OR y = " + str(r))
    print("p = " + str(p))
        
