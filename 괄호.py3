n = int(input())
for i in range(n):
    res = 0
    PS = list(input())
    for _ in PS:
        if _ == '(':
            res += 1
        else:
            res -= 1
        if res < 0:
            print("NO")
            break
    if res > 0:
        print("NO")
    if res ==0 :
        print("YES")
