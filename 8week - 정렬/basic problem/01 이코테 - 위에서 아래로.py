n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))

res.sort(reverse=True)
for item in res:
    print(item, end=' ')
