N, M = map(int, input().split())
C = list(map(int, input().split()))
ans = []

for i in range(N-2):
  for j in range(N-2):
    for _ in range(N-2):
      if i+j+_+2 >= N:
        break
      if C[i] + C[i+j+1] + C[i+j+_+2] <= M:
        ans.append(C[i] + C[i+j+1] + C[i+j+_+2])
ans.sort()
print(ans[-1])