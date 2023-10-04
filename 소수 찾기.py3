import sys

N = int(input())
ans = 0

num = list(map(int, sys.stdin.readline().split()))
  
for i in num:
  if i != 1:
      for j in range(i):
        if j != 0 and j !=1:
          if i % j == 0:
            ans -= 1
            break
      ans += 1  
print(ans)