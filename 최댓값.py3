arr = []
max = 0
for i in range(9):
  arr.append(int(input()))
for i in arr:
  if max < i:
    max = i

print(max)
for i in range(9):
  if arr[i] == max:
    print(i+1)