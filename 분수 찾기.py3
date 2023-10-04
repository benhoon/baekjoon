X = int(input())

for i in range(X):
  if (i+1)*(i+2)/2 >= X:
    j = (i+1)*(i+2)/2 - X
    if (i+1)%2 == 0:#짝수
      ans_son = int(i+1 - j)
      ans_mom = int(1 + j)
    else:
      ans_son = int(1 + j)
      ans_mom = int(i+1 - j)
    break
  else:
    continue
print(ans_son, end = '')
print('/', end = '')
print(ans_mom, end = '')