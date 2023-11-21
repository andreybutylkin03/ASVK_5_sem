import os

with open("1.in", "r") as fd:
    s = os.path.getsize("1.in")
    txt = fd.read((s - 1) // 6)

print(txt)
