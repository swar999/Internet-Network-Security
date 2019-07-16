import math
print("enter the two prime number")
p,q=(input().split(" "))
p,q=int(p),int(q)
m=int(input("enter the Msg ="))
N=p*q
Qn=(p-1)*(q-1)
for i in range(2,Qn):
    if(math.gcd(i,Qn)==1):
        e=i
        break
    else:
        pass
for i in range(1,100000):
    d=int((1+i*Qn)/e)
    if(d<Qn and d>0 and (d*e)%Qn==1):
        break
    else:
        pass
print(d)
print("encryption is ")
c=(m**e)%N
print(c)
print("decryption is")
M=(c**d)%N
print(M)