

N = input()
  
ans = 0

for _ in range (len(N)):
  if N[_] == 'A' or N[_] == 'B' or N[_] == 'C':
    ans = ans + 3
  if N[_] == 'D' or N[_] == 'E' or N[_] == 'F':
    ans = ans + 4
  if N[_] == 'G' or N[_] == 'H' or N[_] == 'I':
    ans = ans + 5
  if N[_] == 'J' or N[_] == 'K' or N[_] == 'L':
    ans = ans + 6
  if N[_] == 'M' or N[_] == 'N' or N[_] == 'O':
    ans = ans + 7
  if N[_] == 'P' or N[_] == 'Q' or N[_] == 'R' or N[_] == 'S':
    ans = ans + 8
  if N[_] == 'T' or N[_] =='U' or N[_] == 'V':
    ans = ans + 9
  if N[_] == 'W' or N[_] == 'X' or N[_] == 'Y'or N[_] == 'Z':
    ans = ans + 10

print(ans)