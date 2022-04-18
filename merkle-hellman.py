import random
import math

def createW(length):
    w = []
    for i in range(length):
        w.append(sum(w)+random.randint(5,10**6))
    return(w)

def createR(q):
    r = q + random.randint(5,10**4)
    if(math.gcd(q,r)==1):
        return(r)
    else:
        while(math.gcd(r,q)!=1):
            r+=1
        return(r)

def createB(w,q,r):
    b = []
    for i in(w):
        b.append((i*r)%q)
    return(b)

def getBinaryList(text):
    binList = []
    for i in(text):
        binary = bin(ord(i))[2:]
        if(len(binary)<8):
            binary = '0'*(8-len(binary))+binary
        for j in(binary):
            binList.append(j)
    return(binList)

def encrypt(binList,b):
    encrypted = 0
    for i in range(len(binList)):
        encrypted += int(binList[i]) * int(b[i])
    return(encrypted)

def decrypt(w,ci):
    binList = []
    temp = ci
    for i in range(len(w)-1,-1,-1):
        if(temp>=w[i]):
            binList.append(1)
            temp-=w[i]
        else:
            binList.append(0)
    binList.reverse()
    return(binToText(binList))

def binToText(binList):
    index = 0
    text = ''
    while(index<len(binList)):
        charBin = ''
        for i in range(index,index+8):
            charBin += str(binList[i])
        text += chr(int(charBin,base=2))
        index+=8
    return(text)

def calculateS(r, q):
    q0 = q
    y = 0
    x = 1

    while (r > 1):

        qu=r//q
        t=q
        q=r%q
        r=t
        t=y
        y=x-qu*y
        x=t
    if(x<0):
        x=x+q0
    return(x)

print("\n\n"+20*"*"+"Merkle-Hellman Test"+20*"*")

text = input("\n\nEnter the text you want to encrypt : ")

binList = getBinaryList(text)

w = createW(len(binList))

q = sum(w)+random.randint(5,10**6)

r = createR(q)

b = createB(w,q,r)

c = encrypt(binList,b)

s = calculateS(r,q)

ci = (c*s)%q

decrypted = decrypt(w,ci)

print("\n\ntext:",text)

print("\n\nencrypted=",c)

print("\n\ndecrypted=",decrypted)

print("\n\n"+60*"*")
