import sys

arr = [['+']*15 for i in range(5)]
S = ['0']*5
ans = []
res = []
answer = []
for i in range(5):
  S[i] = sys.stdin.readline()
  for j in range(len(S[i])-1):
    arr[i][j] = S[i][j]

for i in range(15):
  ans.append(arr[0][i])

for i in range(15):
    for j in range(4):
      ang = ans[i]
      ing = arr[j+1][i]
      ong = ang + ing
      ans[i] = ong


for i in ans:
  for j in i:
    temp = j.replace("\n", "+")
    res.append(temp)
for j in res:
  temp = j.replace("+", "")
  answer.append(temp)
  
for i in range(len(answer)):
  print(answer[i], end = '')