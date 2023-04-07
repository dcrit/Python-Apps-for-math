# c=(m+k)mod N (encryption)
# m=(c-k)mod N (decrpytion)

choice = int(input("1 for encyption or 2 for decryption: "))

# encryption
if choice == 1:
    m = int(input("Enter m: "))
    k = int(input("Enter k: "))
    n = int(input("Enter n: "))

    e = (m + k) % n

    print(str(e))
# decrpytion 
elif choice == 2:
    c = int(input("Enter c: "))
    k = int(input("Enter k: "))
    n = int(input("Enter n: "))

    d = (c-k) % n
    print(str(d))


# Suppose Alice and Bob use the simple encryption 
# scheme in which c = (m + k) mod N and m = (c − k) mod N. 
# Suppose that Eve knows that N = 4657. Suppose that she also 
# manages to learn that the message m corresponding to c = 1322 is 3411. 
# Can she infer the value for k? What is k?


# Solution
# If c = (m + k) mod N, then k = (c - m) mod N

 #k = (1322 - 3411) mod 4657 = -2089 mod 4657 = 2568