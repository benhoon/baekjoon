import sys
sub = [0] * 20
time = [0] * 20
score = [0] * 20
abc = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
s =   [4.5,  4.0,   3.5, 3.0,   2.5,  2.0,  1.5,  1.0,  0.0 ]
sum = 0 #학점*과목평점 총합
t_sum = 0 #학점 총합

for i in range(20):
  sub[i], time[i], score[i] = map(str, sys.stdin.readline().split())
  time[i] = float(time[i])
  
  for j in range(9):
    if score[i] == abc[j]:
      score[i] = s[j]  #과목 평점 변환

for _ in range(20):
  if score[_] != 'P':
    sum = sum + (time[_] * float(score[_]))
    t_sum += time[_]

print(sum / t_sum)
    