hex={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
msg=input("enter the 64 bit msg in hex number =")
key=input("enter the 64 bit key in hex number =")
ep=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
ip=[58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
pc1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
pc2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
left=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
def sbox(p):
    
def xor(s1,s2):
    n=len(s1)
    z=""
    for i in range(0,n):
        if(s1[i]==s2[i]):
            z+="0"
        else:
            z+="1"
    return z
def shift(s,left,round):
    n=len(s)
    w=left[round]
    s1=""
    s2=""
    s3=""
    s4=""
    for i in range(0,n/2):
        s1+=s[i]
        s2+=s[i+n/2]
    for i in range(0,n/2):
        if(i+w<n/2):
            s3+=s1[i+w]
            s4+=s2[i+w]
        else:
            s3+=s1[(i+w)%(n/2)]
            s4+=s2[(i+w)%(n/2)]
    return s3+s4   
def pc1inkey(key):
    s=hextobin(key)
    b=tra(s,pc1)
    return b
def hextobin(s):
    z=""
    for i in range(0,len(s)):
        z+=hex[s[i]]
    return z
def tra(s,k):
    a=""
    for i in range(0,len(k)):
        a+=s[int(k[i])-1]
    return a
def kr(key,round):
    if(round==0):
        s=pc1inkey(key)
        q=shift(s,left,round)
        return tra(q,pc2)
    else:
        q=shift(q,left,round)
        return tra(q,pc2)
def pro(msg,key,ip,pc1,pc2,left):
    s=hextobin(msg)
    q=tra(s,ip)
    n=len(q)
    le=""
    re=""
    for i in range(0,n/2):
        le+=q[i]
        re+=q[i+n/2]
    for i in range(0,16):
        s1=tra(re,ep)
        s2=kr(key,i)
        s3=xor(s1,s2)
        s6=xor(s5,le)
        le=re
        re=s6
    s7=re+le
    return tra(s7,iip)
