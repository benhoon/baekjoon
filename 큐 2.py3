import sys
from collections import deque
N = int(input())
que = deque([])
for i in range(N):
  ord = sys.stdin.readline().split()

  if ord[0] == 'push':
    que.append(ord[1])

  elif ord[0] == 'pop':
    if que:
      print(que.popleft())
    else:
      print('-1')

  elif ord[0] == 'size':
    print(len(que))

  elif ord[0] == 'empty':
    if len(que) == 0:
      print('1')
    else:
      print('0')

  elif ord[0] == 'front':
    if que:
      print(que[0])
    else:
      print('-1')

  elif ord[0] == 'back':
    if que:
      print(que[-1])
    else:
      print('-1')