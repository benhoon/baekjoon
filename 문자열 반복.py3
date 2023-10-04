import sys

T = int(input())
for _ in range(T):
  R, S = sys.stdin.readline().split()
  R = int(R)
  for i in range(len(S)):
    print(R*S[i], end = '')
  print()