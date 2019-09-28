import hashlib
k=input("enter the mag=")
e=hashlib.sha1(k.encode())
print(e.hexdigest())
