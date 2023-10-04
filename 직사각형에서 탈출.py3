x, y, w, h = map(int, input().split())

result = [x, y, w-x, h-y]
ans = x
for i in result:
  if ans > i:
    ans = i
print(ans)