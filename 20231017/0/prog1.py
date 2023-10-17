import timeit

s = input()

num, timing = timeit.Timer(stmt=s, globals=globals()).autorange()
per_run = timing/num
print(per_run)
