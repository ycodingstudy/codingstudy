n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9


def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우 최솟값 최댓값 업뎃
    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, max)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))  # 나머지를 제거하기 위함
            div += 1


dfs(1, data[0])

print(max_val)
print(min_val)
