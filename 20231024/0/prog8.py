import itertools

res = list(itertools.product("abcdefgh", map(str, range(1, 9))))
for i, j in res:
    print(f"{i}{j}")
