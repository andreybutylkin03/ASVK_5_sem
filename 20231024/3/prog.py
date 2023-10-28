import itertools

print(*list(filter(lambda x: x.count('TOR') == 2, map(''.join, itertools.product("ORT", repeat=int(input()))))), sep=', ')
