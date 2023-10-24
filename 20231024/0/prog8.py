import itertools

print(*[f"{i}{j}" for i, j in list(itertools.product("abcdefgh", map(str, range(1, 9))))], sep='\n')

