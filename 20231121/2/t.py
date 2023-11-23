import sys
sys.getdefaultencoding()

while s := sys.stdin.readline():
    print(s.encode("CP1251", errors='replace').decode("latin1", errors='replace'), end='')
