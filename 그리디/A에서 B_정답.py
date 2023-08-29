# https://www.acmicpc.net/problem/16953

num , target = map(int, input().split())
cnt = 1
while num != target:
    cnt += 1
    temp = target
    if target % 10 == 1:
        target //= 10
    elif target % 2 == 0:
        target //= 2
    if temp == target:
        print(-1)
        break
else:
    print(cnt)