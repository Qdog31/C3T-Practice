import codecs

#This code can crack a rot13 code. 

with open("rot13.enc") as f: 
    enc = f.readline().rstrip()
    flag = codecs.decode(enc, 'rot_13')
print(flag)
