stick = list(map(int, input().split()))
stick.sort()
ans = 0

if stick[0] + stick[1] <= stick[2]:
  while (True):
    stick[2] = stick[2] -1
    if stick[0] + stick[1] > stick[2]:
      break
      


for i in stick:
  ans = ans+ i

print(ans)