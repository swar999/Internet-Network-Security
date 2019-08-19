def texttobox(text):
    s1=[]
    ___=0
    for _ in range(4):
        s=[]
        for __ in range(4):
            s.append(text[___]+text[___+1])
            ___+=2
        s1.insert(_,s)
    return(s1)
def xor(box1,box2):
    s1=[]
    for _ in range(4):
        s=[]
        for __ in range(4):
            c1=hex(int("0x"+(box1[_][__])[0:1],16) ^ int("0x"+(box2[_][__])[0:1],16))[2:]
            c2=hex(int("0x"+(box1[_][__])[1:2],16) ^ int("0x"+(box2[_][__])[1:2],16))[2:]
            s.append(c1+c2)
        s1.insert(_,s)
    return s1
def SubBytes(box,sbox):
    s1=[]
    for _ in range(4):
        s=[]
        for __ in range(4):
            c1,c2=int("0x"+box[_][__][:1],16),int("0x"+box[_][__][1:2],16)
            s.append(sbox[c1][c2])
        s1.insert(_,s)
    return s1
def ShiftRows(box):
    s1=[]
    for _ in range(4):
        s=["","","",""]
        for __ in range(4):
            ___=__-_
            if(___<0):
                ___=___+4
            s[___]=box[_][__]
        s1.insert(_,s)
    return s1
def mult(b1):
    b1="0x"+b1
    b1=bin(int(b1,16))[2:].zfill(8)
    if b1[0]=="1":
        b1="0b"+b1[1:]+0
        b2="0x1b"
        b1=hex(int(b1,2) ^ int(b2,16))[2:].zfill(2)
        return b1
    return hex(int("0b"+b1,2))[2:].zfill(2)
def MixColumns(box):
    m=[['02','03','01','01'],['01','02','03','01'],['01','01','02','03'],['03','01','01','02']]
    # s1=[]
    for _ in range(4):
        b=[]
        for __ in range(4):
            b.insert(__,box[__][_]) 
        c1=0
        for __ in range(4):
            if m[_][__]=="02":
                c1+=int("0x"+mult(b[__]),16)
            elif m[_][__]=="03":
                c1+=int("0x"+mult(b[__]),16) + int("0x"+b[__],16)
            elif m[_][__]=="01":
                c1+=int("0x"+b[__],16)
        

# msg=input("enter the number(128 bit) msg in hex form")
# key=input("enter the number(128 bit) msg in hex form")
msg="328831e0435a3137f6309807a88da234"
key="2b28ab097eaef7cf15d2154f16a6883c"
msgbox=texttobox(msg)
keybox=texttobox(key)
# print(msgbox,keybox)
a=xor(msgbox,keybox)
# print(a)
sbox=  [["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"],["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"],["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"],["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"],["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"],["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"],["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"],["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"],["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"],["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"],["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"],["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"],["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"],["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"],["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"],["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]]
b=SubBytes(a,sbox)
# print(b)
c=ShiftRows(b)
# print(c)
MixColumns(c)