import sys
a,b = (1,1)
while a != 0 and b != 0:
  a,b = map(int, sys.stdin.readline().split())
  if a != 0 and b != 0:
    print(a + b)
  