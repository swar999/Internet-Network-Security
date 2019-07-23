def enc(l1,s):
    s=s.lower()
    count={}
    rev={}
    l2=[]
    for i in s:
        if(ord(i)>96 and ord(i)<123):
            count[i]=s.count(i)
    for i,k in sorted(count.items(),key=lambda a:a[1],reverse=True):
        rev[i]=k
        l2.append(i)
    for i,k in zip(l1,l2):
        s=s.replace(k,i)
    print(s)
    print(l2)
l1=["E","T","A","O","I","N","S","R","H","D","L","U","C","M","F","Y","W","G","P","B","V","K","X","Q","J","Z"]
s="The view object will reflect any changes done to the dictionary, see example below."
enc(l1,s)
s="THE YIED ALWENT DIOO UEGOENT SRC NHSRPEM FARE TA THE FINTIARSUC, MEE EBSVKOE LEOAD."
enc(l1,s)