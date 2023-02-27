from egcd import egcd 
print(egcd(15,26))

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!= 1: 
        raise Exception("Modular inverse does not exist")
    else: 
        return x%m 
#This is 15^-1, then mod it by 26
print(pow(15,-1,26))


