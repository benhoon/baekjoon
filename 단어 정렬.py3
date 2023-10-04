import sys

N = int(input())
I = []
S = []
check = 0
count = 0

for i in range(N):
  I.append(sys.stdin.readline().rstrip())

for i in I:
  if i not in S:
    S.append(i)

S.sort(key = len) #길이 기준 배열

for i in range(len(S)-1):
  res = 0
  if len(S[i]) == len(S[i+1]):
    count += 1
    check = len(S[i])
  elif check > 0:
    S[i-count+1:i+1] = sorted(S[i-count+1:i+1])
    check = count = 0
    res = 1
  if res == 0 and count > 0:
    S[i-count+1:i+2] = sorted(S[i-count+1:i+2])

  
for i in S:
  print(i)