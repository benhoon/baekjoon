n,k = map(int, input().split())
R = list(range(1,n+1))
x = k
print('<',end='')
while len(R) > 0:
    if k > len(R):
        k -= len(R)
    else:
        print(R[k-1],end= '')
        if len(R) != 1:
            print(', ',end ='')
        R.pop(k-1)
        k = k-1 + x
print('>',end='')