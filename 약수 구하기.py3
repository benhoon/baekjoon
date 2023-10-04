N, K = map(int, input().split())
ans = [0] * N
j = -1

for i in range(N):
  if N % (i+1) == 0:
    j = j+1
    ans[j] = i+1
    
print(ans[K-1])