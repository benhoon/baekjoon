M = int(input())
N = int(input())
sosu = []
remove = []
for i in range(M, N+1, 1):
  sosu.append(i)
sum = 0

for i in sosu:
  if i == 1:
    sosu.remove(i)
  else:
    for j in range(i):
      if j > 1:
        if i % j == 0:
          remove.append(i)
          break
for i in remove:
  sosu.remove(i)
if len(sosu) == 0:
  print('-1')
else:
  for i in sosu:
    sum += i
  print(sum, sosu[0])