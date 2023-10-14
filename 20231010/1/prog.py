from fractions import Fraction

def P(kf, x):
    st = len(kf) - 1
    ans = Fraction("0")
    for i in range(st + 1):
        ans += kf[-(i + 1)] * (x ** i)
    return ans

a = list(map(Fraction, input().split(',')))
s = a[0]
w = a[1]
a_st = a[2]
a_kf = []
for i in range(3, 3 + int(a_st) + 1):
    a_kf.append(a[i])
b_st = a[4 + int(a_st)]
b_kf = []
for i in range(5 + int(a_st), 6 + int(a_st + b_st)):
    b_kf.append(a[i])

ar = P(a_kf, s)
br = P(b_kf, s)

print(False if br == 0 else ar / br == w)
