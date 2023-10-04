n = []
sum = 0
for i in range(5):
  n.append(int(input()))
for i in n:
  sum += i
n.sort()

print(int(sum/5))
print(n[2])