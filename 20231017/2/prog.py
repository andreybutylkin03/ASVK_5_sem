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
        if s.split()[0] == 'quit':
            nf += 1
            id1 = s.find('"')
            id2 = s[::-1].find('"')
            print(s[id1 + 1:-(id2 + 1)].format(nf, ns))
            sys.exit()
        else:
            foo_n, *args = s.split()
            *sarg, evdef = foo[foo_n]
            if len(sarg) == 1 and len(args) != 1:
                args = []
                args.append(s[(s.find('"') + 1): -(s[::-1].find('"') + 1)])
            d = dict()
            for i in range(len(args)):
                try:
                    d |= {f"{sarg[i]}" : eval(args[i])}
                except:
                    d |= {f"{sarg[i]}" : args[i]}
   
            print(eval(evdef, globals() | d))
