import enchant 
from caesarcipher import CaesarCipher 

d = enchant.Dict("en_US")

with open("caesar.enc") as f: 
    enc = f.readline().rstrip()

    flags = []

    for i in range(1,26):
        flag = CaesarCipher(enc,offset=i).decoded

        score = 0 
        for word in flag.split(): 
            if d.check(word):
                score += 1 
        flags.append((score,flag))

    flags.sort(reverse=True)
    for flag in flags:
        print(f"{flag[0]}: {flag[1]}")
        
