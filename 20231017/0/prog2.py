import string

s = input()
ss = set(string.ascii_lowercase)
gg = set("euyioa")
ss -= gg

print(len(set(s) & gg), len(set(s) & ss))
