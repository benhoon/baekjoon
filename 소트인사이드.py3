N = input()
list = []
for i in N:
  list.append(int(i))
list.sort()
s = len(list)

for i in range(s):
  print(list[-i-1], end = '')