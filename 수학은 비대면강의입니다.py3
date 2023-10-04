a,b,c,d,e,f = map(int, input().split())
ansx = ansy =0
for x in range(-999,1000,1):
  for y in range(-999,1000,1):
    if a*x + b*y == c and d*x + e*y == f:
      ansx = x
      ansy = y
      break
  if ansy == y:
    break
print(ansx, ansy)