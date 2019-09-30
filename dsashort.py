p = 303287
q = 151643
alp = 252
x = 252 #int(input("Please enter your \"X\": "))
r = 0
s = 0
d = 20 #int(input("Enter your private Key: "))
eph = 1542 #int(input("Enter your Ephernal Key: "))

def xgcd(b, n):         # computing multiplicative inverse
    print("xgcd, b: ", b)
    print("xgcd, n: ", n)
    for z in range(0, n):
        if (((b * z) % n) == 1):
            #print(z)
            return z;


def gen_pub_key(alp, p, d):
    bet = (alp ** d) % p
    print("Bet: ", bet)
    return bet


def gen_sig(alp, p, q, x, eph, d):
    r = ((alp ** eph) % p) % q
    print("r: ", r)
    eph_inv = xgcd(eph, p)
    print("eph_inv: ", eph_inv)
    s = (((x + d) * r) * eph_inv) % q
    print("s: ",s)
    return (r, s)


def sig_veri(s, r, p, q, x, alp, bet):
    print("sig_veri: p: ", p)
    w = (xgcd(s, p)) #% q
    print("w: ", w)
    u1 = (w * x) % q
    print("u1: ", u1)
    u2 = (w * r) % q
    print("u2: ", u2)
    v = (((alp * u1) * (bet * u2) % p)) % q
    print("v: ", v)
    t = r % q
    if (v == t):
        print("Die Signatur ist Valide!")
    else:
        print("Die Signatur ist nicht Valide!")

bet = gen_pub_key(alp, p, d)

sig = gen_sig(alp, p, q, x, eph, d)
r = int(sig[0])
print("sig 0, r: ", r)
s = int(sig[1])
print("sig 1, s", s)


sig_veri(s, r, p, q, x, alp, bet)
