N = int(input())

for i in range(N):
  print(" " * (N-i-1), end ="")
  print("*" * (i+1), end = "")
  print("*" * (i))

for i in range(N):
  print(" " * (i+1), end = "")
  print("*" * (N-i-1), end = "")
  print("*" * (N-i-2))