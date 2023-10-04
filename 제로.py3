k = int(input())
note = []

for i in range(k):
    n = int(input())
    if n !=0:
        note.append(n)
    else:
        note.pop()
print(sum(note))