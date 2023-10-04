while(True):
  S = list(map(int, input().split()))
  S.sort()

  if S[0]==S[1]==S[2]==0:
    break

  elif S[0]+S[1] <= S[2]:
    print("Invalid")

  else:
    if S[0]==S[1] or S[0]==S[2] or S[1]==S[2]:
      if S[0]==S[1]==S[2]:
        print("Equilateral")
      else:
        print("Isosceles")
    else:
      print("Scalene")