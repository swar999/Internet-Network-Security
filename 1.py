def ens(s,k):
    l=len(s)
    s1=""
    # while i<l:
    #     sz=s[i]
    #     j=0
    #     for x in l1:
    #         if(x!=sz):
    for i in s:
        if(i!=" "):
            s1+=l1[(ord(i)-97)+k-1]
    print(s1)
s="hello world"
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=4
ens(s,k)