n = input()
score = list(map(int, input().split()))
mymax = max(score)
mysum = sum(score)

print(mysum * 100 / mymax / int(n))