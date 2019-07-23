s=input("enter the mas=")
k=int(input("enter the key="))
l=[[] for j in range(k)]
print(l)
for i in range(1,len(s),2*k-1):
    for j in range(1,k):
        print(j)
        l[j-1].append(s[i+j-2])
        print(l)
    for j in range(k,2*k-1):
        print(j)
        m=0
        l[j-m-1].append(s[j+i-2])
        m+=1
        print(l)
print(l)
