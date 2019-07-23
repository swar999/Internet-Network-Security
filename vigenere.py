s=input("enter the msg=")
s1=input("enter the key=")
k=""
for i in range(0,len(s)):
    k+=chr(((ord(s[i])+ord(s1[i])-97-97)%26)+97)
print(k)