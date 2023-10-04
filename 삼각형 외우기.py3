A = []
for i in range(3):
  A.append(int(input()))

sum = A[0] + A[1] + A[2]

if sum == 180:
  if A[0]==A[1] or A[0]==A[2] or A[1]==A[2]:
    if A[0]==A[1]==A[2]:
      print("Equilateral")
    else:
      print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")