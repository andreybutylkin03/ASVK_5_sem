with open("1.in", "rb") as fd:
    bb = fd.read()

with open("1.in", "wb") as fd:
    fd.write(bb[len(bb) // 2:])
    fd.write(bb[:len(bb) // 2])

