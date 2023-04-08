import math
 
# step 1
p = int(input("Enter p: "))
q = int(input("Enter q: "))
 
# step 2
n = p*q
print("n =", n)
 
# step 3
phi = (p-1)*(q-1)
print("Phi = " + str(phi))
 
# step 4
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
 
print("e =", e)
# step 5
k = 2
d = ((k*phi)+1)/e
print("d =", d)
print("Public key: " + str({e, n}) )
print("Private key: " + str({d, n}))
 
# plain text
msg = 11
print("Original message: " + str({msg}))
 
# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print("Encrypted message: " + str({C}))
 
# decryption
M = pow(C, d)
M = math.fmod(M, n)
 
print("Decrypted message: " + str({M}))