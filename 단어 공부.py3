S = input()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = [0] * 26
max = 0
same = 0

for i in range(26):
  n[i] = S.count(alpha[i]) + S.count(alpha[i+26])
for i in range(26):
  if max < n[i]:
    max = n[i]
    ans = i
for _ in range(26):
  if max == n[_]:
    same += 1
if same >1:
  print("?")
else:
  print(alpha[ans])