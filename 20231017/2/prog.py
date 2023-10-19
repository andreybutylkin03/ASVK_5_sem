from math import *
import sys

foo = {}
nf, ns = 0, 0

while s := input():
    if s[0] == ':':
        ns += 1
        nf += 1
        foo_n, *args, s_foo = s[1:].split()

        foo[foo_n] = (*args, s_foo)
    else:
        ns += 1
        if len(s) >= 4 and s[:4] == "quit":
            nf += 1
            id1 = s.find('"')
            id2 = s[::-1].find('"')
            print(s[id1 + 1:-(id2 + 1)].format(nf, ns))
            sys.exit()
        else:
            foo_n, *args = s.split()
            *sarg, evdef = foo[foo_n]
            d = {f"{sarg[i]}" : eval(args[i]) for i in range(len(args))}
            print(eval(evdef, globals() | d))
