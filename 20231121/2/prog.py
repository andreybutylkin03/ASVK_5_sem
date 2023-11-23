import sys
sys.getdefaultencoding()

while s := sys.stdin.readline():
    print(s.encode("latin1", errors='replace').decode("CP1251", errors='replace'), end='')
