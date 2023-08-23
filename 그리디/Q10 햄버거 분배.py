# https://www.acmicpc.net/problem/19941

N, K = map(int, input().split())
arr = list(input())
rangeList = [i for i in range(-K, K + 1)]  # 먹을 수 있는 범위 (음수부터)

answer = 0
for i in range(N):
    if arr[i] == "P":
        for j in rangeList:
            now = i + j
            if 0 <= now < N and arr[now] == "H":
                arr[now] = "E"  # Eat 처리
                answer += 1
                break

print(answer)
