N = int(input())
start = 1


while(True):
  sum = start
  start = str(start)
  for i in range(len(start)):
    sum = sum + int(start[i])
  start = int(start)
  if sum == N or start > N:
    break
  start += 1
if sum == N:
  print(start)
if start > N:
  print(0)