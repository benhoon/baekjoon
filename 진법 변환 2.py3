N, B = map(int, input().split()) # 입력
na = []
mox = N
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while(True):
  na.append(mox%B)
  mox = mox//B
  if mox == 0:
    break
  if mox < B and mox > 0:
    na.append(mox)
    break
s = len(na)

for i in range(s):
  for j in range(26):
    if na[i] == j+10:
      na[i] = alpha[j]
for i in range(s):
  print(na[-(i+1)], end = '')