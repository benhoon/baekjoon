import sys

n = int(input())
stk = []
ord = []

for i in range(n):
  ord = list(map(int,sys.stdin.readline().split()))
  
  if ord[0] == 1:
    stk.append(ord[1])
  if ord[0] == 2:
    if len(stk) > 0:
      print(stk[-1])
      stk.pop()
    else:
      print(-1)
  if ord[0] == 3:
    print(len(stk))
  if ord[0] == 4:
    if len(stk) == 0:
      print(1)
    else:
      print(0)
  if ord[0] == 5:
    if len(stk) > 0:
      print(stk[-1])
    else:
      print(-1)