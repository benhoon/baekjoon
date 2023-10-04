N, k = input().split()
k = int(k)
score = list(map(int, input().split()))

score.sort()

print(score[-k])