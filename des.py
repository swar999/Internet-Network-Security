def tra(s,k):
    a=""
    for i in range(0,len(k)):
        # print(k[i])
        # print(s[int(k[i])-1])
        a+=s[int(k[i])-1]
        # print(a)
    # print(a)
    return a
def hextobin(s):
    z=""
    for i in range(0,len(s)):
        z+=hex[s[i]]
    # print(z)
    return z
def pc1inkey(key):
    s=hextobin(key)
    # print(s)
    b=tra(s,pc1)
    print(b)
    
hex={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
# msg=input("enter the 64 bit msg in hex number =")
key=input("enter the 64 bit key in hex number =")
pc1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
pc2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
left=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
# print(len(pc1),len(pc2),len(left))
pc1inkey(key)
