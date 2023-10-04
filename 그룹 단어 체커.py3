N = int(input())
S = []
Sn = [0] * N
ans = 0
ex = 0

for i in range(N):
  S.append(input())
for i in range(N):
  for j in range(len(S[i])-1):#j 0123
    for a in range(j, len(S[i])-1, 1):  ## 여기 고치기 a+1 1234
      if S[i][j] != S[i][a + 1]:
        ex = 0
        continue
      elif j + 1 == a + 1:
        ex = 1
        continue
      elif ex == 1:
        continue
      else:
        Sn[i] = -1
        break
  if Sn[i] == 0:
    Sn[i] = 1
  else:
    Sn[i] = 0

for i in range(N):
  ans = ans + Sn[i]
print(ans)