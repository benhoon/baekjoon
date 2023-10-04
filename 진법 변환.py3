N, B= input().split()
B = int(B)
S = [0] * len(N)
for i in range(len(N)):
  S[i] = N[i]
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
ans = 0

for i in range(len(N)):
  for j in range(26):
    if S[i] == alpha[j]:
      S[i] = j+10
  for j in range(10):
    if S[i] == num[j]:
      S[i] = j

for i in range(len(N)):
  ans += S[i] *(B**(len(N)-i-1))
print(ans)