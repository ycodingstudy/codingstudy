N = int(input())
heights = list(map(int, input().split()))
result = [0] * N

for h in range(N):
    cnt = 0
    t = heights[h]
    for i in range(N):
        if result[i] == 0 and cnt == t:
            result[i] = h + 1
            break
        elif result[i] == 0:
            cnt += 1
print(*result)
