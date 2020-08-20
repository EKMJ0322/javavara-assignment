a, b = map(int, input().split())
for i in range(b):
    scores = []
    c = map(float, input().split())
    scores.append(c)
for j in zip(*scores):
    print(sum(j)/len(j))