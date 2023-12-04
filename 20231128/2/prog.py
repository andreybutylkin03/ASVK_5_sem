import math
import sys

comma = []
label = dict()
control = dict()
variable = dict()
siz_com = 0
flag = [False, 0]

for s in sys.stdin.readlines():
    s = s.split()
    if len(s) == 0: 
        continue

    if s[0][-1] == ':':
        label[s[0][:-1]] = siz_com
        control[siz_com] = len(comma)
        s.pop(0)

    if len(s) == 0:
        continue
 
    pre = flag[0]

    match s:
        case ['stop']:
            comma.append(('stop', ))
            flag[0] = True
        case ['store', num, var]:
            comma.append(('store', num, var))
            flag[0] = True
        case [OP, eax, ebx, edx] if OP in {'add', 'sub', 'div', 'mul'}:
            comma.append((OP, eax, ebx, edx))
            flag[0] = True
        case [CMP, eax, ebx, lab] if CMP in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}:
            comma.append((CMP, eax, ebx, lab))
            flag[0] = True
        case ['out', var]:
            comma.append(('out', var))
            flag[0] = True
        case _:
            if flag[0]:
                flag = [False, siz_com]

    if flag[0]:
        control[siz_com] = len(comma) - 1

    if not pre and flag[0]:
        for i in range(flag[1], siz_com):
            control[i] = control[siz_com]

    siz_com += 1

comma.append(('stop', ))
control[siz_com] = len(comma) - 1 

for com in comma:
    if com[0] in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'} and com[3] not in label.keys():
        sys.exit()

i = 0

while True:
    s = list(comma[control[i]])

    match s:
        case ['stop']:
            sys.exit()
        case ['store', num, var]:
            i += 1
            try:
                variable[var] = float(num)
            except:
                pass
        case [OP, eax, ebx, edx] if OP in {'add', 'sub', 'div', 'mul'}:
            i += 1
            eax = variable.setdefault(eax, 0)
            ebx = variable.setdefault(ebx, 0)

            try:
                match OP:
                    case 'add':
                        variable[edx] = eax + ebx
                    case 'sub':
                        variable[edx] = eax - ebx 
                    case 'div':
                        variable[edx] = eax / ebx
                    case 'mul':
                        variable[edx] = eax * ebx    
            except:
                variable[edx] = math.inf  
        case [CMP, eax, ebx, lab] if CMP in {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}:
            eax = variable.setdefault(eax, 0)
            ebx = variable.setdefault(ebx, 0)

            flag = False

            match CMP:
                case 'ifeq':
                    flag = eax == ebx
                case 'ifne':
                    flag = eax != ebx
                case 'ifgt':
                    flag = eax > ebx
                case 'ifge':
                    flag = eax >= ebx
                case 'iflt':
                    flag = eax < ebx
                case 'ifle':
                    flag = eax <= ebx

            if flag:
                i = label[lab]
            else:
                i += 1
        case ['out', var]:
            i += 1
            print(variable.setdefault(var, 0))

