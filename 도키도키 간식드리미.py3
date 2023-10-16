N = int(input())
line = list(map(int, input().split()))
space = []

for i in range(N):
  check = sorted(space)
  if i+1 in line:
    ans = 1
    a = line.index(i+1)
    for j in range(a):
      space.insert(0,line[0])
      line.pop(0)
    line.pop(0)
  elif space == check:
    ans = 1
    break
  else:
    ans = 0
    break
if ans == 1:
  print("Nice")
else:
  print("Sad")