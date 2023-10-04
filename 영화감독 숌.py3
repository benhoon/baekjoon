N = int(input())
T = '666'
title = []
count = 0

while (True):
  if T.count('666') >= 1:
    title.append([T])
    count += 1
  T = str(int(T) + 1)
  if count == N:
    print(*title[count-1])
    break