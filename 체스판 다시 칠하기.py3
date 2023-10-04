N, M = map(int, input().split())
board = []
for i in range(N):
 board.append(input())
boardT = []
res1 = res2 = 0
ans = []
case1 = []#W먼저
for i in range(8):
  if i%2 == 0:
    case1.append('WBWBWBWB')
  else:
    case1.append('BWBWBWBW')
case2 = []
for i in range(8):
  if i%2 == 0:
    case2.append('BWBWBWBW')
  else:
    case2.append('WBWBWBWB')

for i in range(N-7):
  for j in range(M-7):
    for _ in range(8):
      boardT.append(board[i+_][j:j+8:1])
      
    for a in range(8):
      for b in range(8):
        if case1[a][b] != boardT[a][b]:
          res1 += 1
        if case2[a][b] != boardT[a][b]:
          res2 += 1
    if res1 >= res2:
      ans.append(res2)
    else:
      ans.append(res1)
    boardT = []
    res1 = res2 =0
ans.sort()
print(ans[0])