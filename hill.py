def martix(l):
    l2=[]
    for i in range(0,3):
        b=0
        for j in range(0,3):
            b+=a[i][j]*l[j]
        l2.append(b%26)
    return l2 
def con(z):
    return ord(z)-97
s=input("enter the msg = ")
a=[[17,17,5],[21,18,21],[2,2,19]]
s1=""
l1=[]
l2=[]
s7=""
for i in range(0,len(s),3):
    for j in range(0,3):
        x=con(s[i+j])
        l1.append(x)
    l2=martix(l1)
    for k in l2:
        s7+=chr(k+97)
    l2.clear()
    l1.clear()
print(s7)
        
