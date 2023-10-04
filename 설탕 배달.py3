N = int(input())
ans = []
res = 0
for i in range(N):
  for j in range(N):
    if 3*i + 5*j == N:
      ans.append(i+j)
      res = 1
      break
    if 3*i + 5*j > N:
      break
if res == 0:
  print(-1)

if res == 1:
  ans.sort()
  print(ans[0])