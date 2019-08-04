def sbox(p):
    q = ""
    w = ""
    k = 0
    for i in range(0, len(p)):
        w += p[i]
        if ((i + 1) % 6 == 0):
            k += 1
            q += bintodectobin(w, k)
            w = ""
    return q


def bintodectobin(q, round):
    a = 2 * int(q[0]) + 1 * int(q[5])
    b = 8 * int(q[1]) + 4 * int(q[2]) + 2 * int(q[3]) + 1 * int(q[4])
    if (round == 1):
        m1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
              [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
              [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
              [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
        return dectobin(str(m1[a][b]))
    elif (round == 2):
        m2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
              [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
              [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
              [13, 8, 10, 1, 2, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
        return dectobin(str(m2[a][b]))
    elif (round == 3):
        m3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
              [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
              [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
              [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
        return dectobin(str(m3[a][b]))
    elif (round == 4):
        m4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
              [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 15, 1, 10, 14, 9],
              [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
              [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 5, 14]]
        return dectobin(str(m4[a][b]))
    elif (round == 5):
        m5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
              [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9]]
        return dectobin(str(m5[a][b]))
    elif (round == 6):
        m6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
              [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
              [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
              [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
        return dectobin(str(m6[a][b]))
    elif (round == 7):
        m7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
              [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
              [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
              [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
        return dectobin(str(m7[a][b]))
    elif (round == 8):
        m8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
              [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
              [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
              [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
        return dectobin(str(m8[a][b]))


def dectobin(s):
    s = int(s)
    b = ""
    if (s >= 8):
        b += "1"
        s = s - 8
    else:
        b += "0"
    if (s >= 4):
        b += "1"
        s = s - 4
    else:
        b += "0"
    if (s >= 2):
        b += "1"
        s = s - 2
    else:
        b += "0"
    if (s == 1):
        b += "1"
    else:
        b += "0"
    return b


def pbox(s):
    p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11,
         4, 25]
    k = tra(s, p)
    return k


def xor(s1, s2):
    n = len(s1)
    z = ""
    for i in range(0, n):
        if (s1[i] == s2[i]):
            z += "0"
        else:
            z += "1"
    return z


def shift(s, left, round):
    n = len(s)
    # print(n)
    w = left[round]
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    for i in range(0, int(n / 2)):
        s1 += s[i]
        s2 += s[i + int(n / 2)]
    for i in range(0, int(n / 2)):
        if (i + w < int(n / 2)):
            s3 += s1[i + w]
            s4 += s2[i + w]
        else:
            s3 += s1[(i + w) % int(n / 2)]
            s4 += s2[(i + w) % int(n / 2)]
    return s3 + s4


def pc1inkey(key):
    s = hextobin(key)
    b = tra(s, pc1)
    return b


def hextobin(s):
    z = ""
    for i in range(0, len(s)):
        z += hex[s[i]]
    return z


def tra(s, k):
    a = ""
    # print(len(s), len(k))
    for i in range(0, len(k)):
        a += s[int(k[i]) - 1]
        # print(int(k[i])-1)
        # print(a)
    return a


def kr(key, round, keyvl):
    if (round == 0):
        s = pc1inkey(key)
        # s=hextobin(key)
        q = shift(s, left, round)
        keyvl.append(q)
        # print(len(q))
        return tra(q, pc2)
    else:
        q=keyvl.pop()
        q = shift(q, left, round)
        keyvl.clear()
        # print(len(q))
        keyvl.append(q)
        return tra(q, pc2)


def bintohex(s,hex):
    s2 = ""
    # print(hex,s)
    # print(type(s))
    print(len(s))
    for i in range(0, len(s), 4):
        s1 = ""
        # print(s[i],s[i+1],s[i+2],s[i+3])
        # print(i)
        s1 += s[i]+s[i+1]+s[i+2]+s[i+3]
        # print(s[i + k],s[i + k + 1],s[i + k + 2],s[i + k + 3])
        # k += 4
        print(s1)
        for i, j in hex.items():
            if j == s1:
                s2 += i
        # if k==64:
        #     break
    return (s2)


def pro(msg, key, ip, pc1, pc2, left,keyvl):
    s = hextobin(msg)
    q = tra(s, ip)
    n = len(q)
    # print(n/2)
    le = ""
    re = ""
    for i in range(0, int(n / 2)):
        le += q[i]
        re += q[i + int(n / 2)]
    for i in range(0, 16):
        s1 = tra(re, ep)
        s2 = kr(key, i, keyvl)
        s3 = xor(s1, s2)
        s4 = sbox(s3)
        s5 = pbox(s4)
        s6 = xor(s5, le)
        le = re
        re = s6
    s7 = re + le
    # print(len(re))
    # print(len(le))
    # print(len(s7))
    # print(len(iip))
    return bintohex(tra(s7, iip),hex)


hex = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
       "8": "1000", "9": "1001", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
# msg=input("enter the 64 bit msg in hex number =")
# msg="ffb2194d004dfcfb"
msg = "ab2221abcd132536"
# key=input("enter the 64 bit key in hex number =")
# key="20ba134cdf35"
key = "0000160420116013"
keyvl=[]
ep = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32,
      24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47,
      39, 31, 23, 15, 7]
pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
       55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
left = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
iip = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53,
       21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33,
       1, 41, 9, 49, 17, 57, 25]
h = pro(msg, key, ip, pc1, pc2,left,keyvl)
print(h)
