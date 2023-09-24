import sys

n = int(input())
graph = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    graph.append(lst)

visit = [0 for _ in range(n) ]

min_value = sys.maxsize

def backTracking(depth, idx):
    global min_value
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    power1 += graph[i][j] # 스타트 팀
                elif not visit[i] and not visit[j]:
                    power2 += graph[i][j] # 링크 팀
        min_value = min(min_value, abs(power1-power2)) # 스타트 팀 링크 차이
        return

    for i in range(idx, n): # n이 4일때 첫 번째 range(0, 4)
        if not visit[i]:
            visit[i] = True
            backTracking(depth + 1, i + 1) # range(1, 1)
            visit[i] = False

backTracking(0, 0)
print(min_value)