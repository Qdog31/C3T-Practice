import enchant 
from caesarcipher import CaesarCipher 

d = enchant.Dict("en_US")

#This file I am opening is the declaration of independence encoded differently for each line. 

#Creates code to decode the first line 
def solve(enc): 
    flags = []

    for i in range(1,26):
        flag = CaesarCipher(enc,offset=i).decoded

        score = 0 
        for word in flag.split(): 
            if d.check(word):
                score += 1 
        flags.append((score,flag))

    flags.sort(reverse=True)
    return flags[0]
#Actually decrypts line   
with open("caesar2.enc") as f:
    #enc means "line", so the below code is "for each line in the file, do....."
    for enc in f: 
        x = enc.rstrip()
        print(solve(x))
