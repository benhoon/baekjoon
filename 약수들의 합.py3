while(True):
  n = int(input())
  j = -1
  yak = [0]*n
  sum = 0
  if n == -1:
    break
  
  for i in range(n):
    if n % (i+1) == 0:
      j += 1
      yak[j] = i+1

  for i in range(j):
    sum += yak[i]

  if n == sum:
    print(n, '=', yak[0], end = '')
  else:
    print(n, end = ' is NOT perfect.')
  for i in range(j-1):
    if n == sum:
      print(' +', yak[i+1], end = '')
  print('')