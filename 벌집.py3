N = int(input())
a = 1

for i in range(N):
  if N == 1:
    ans = 1
  if a < N and N <= a+6*i:
    ans = i+1
    break
  else:
    a = a + 6*i 
    continue

print(ans)