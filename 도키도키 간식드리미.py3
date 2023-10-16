from collections import deque
import sys

n = int(input())
dec = deque([])
for i in range(n):
    ord = sys.stdin.readline().split()
    if ord[0] == '1':
        dec.appendleft(ord[1])
    elif ord[0] == '2':
        dec.append(ord[1])
    elif ord[0] == '3':
        if dec:
            print(dec[0])
            dec.popleft()
        else:
            print("-1")
    elif ord[0] == '4':
        if dec:
            print(dec[-1])
            dec.pop()
        else:
            print("-1")
    elif ord[0] == '5':
        print(len(dec))
    elif ord[0] == '6':
        if dec:
            print("0")
        else:
            print("1")
    elif ord[0] == '7':
        if dec:
            print(dec[0])
        else:
            print("-1")
    elif ord[0] == '8':
        if dec:
            print(dec[-1])
        else:
            print("-1")