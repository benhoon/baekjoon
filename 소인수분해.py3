N = int(input())

if N == 1:
  print('')

else:
  for i in range(N):
    if i > 0:
      while(True):
        if N%(i+1) == 0:
          N = N/(i+1)
          print(i+1)
        else:
          break