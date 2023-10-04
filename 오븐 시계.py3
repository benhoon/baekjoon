A, B = map(int, input().split())

C = int(input())

if B+(C%60) > 59:
  B = B+(C%60) - 60
  if A == 23:
    A = 0
  else:
    A = A + 1
else:
    B = B+(C%60)
if C//60 > 0:
  if A+(C//60) > 23:
    A = A+(C//60) - 24
  else:
    A = A+(C//60)
print(A, B)