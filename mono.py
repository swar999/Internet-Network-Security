def enc(s,bc):
    s1=""
    for x in s:
        if(x!=" "and x!=x.upper()):
            s1+=bc.get(x)
        elif(x!=" " and x==x.upper()):
            z=bc.get(x.lower())
            s1+=z.upper()
        else:
            s1+=" "
    return s1
bc={"a":"b","b":"g","c":"a","d":"c"}
s="Abc bca"
s1=enc(s,bc)
print(s1)