import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 인접리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)  # visited 역할을 함께 함


def bfs(x):
    q = deque([x])
    distance[x] = 0

    while q:
        cur = q.popleft()
        for neighbor in graph[cur]:
            if distance[neighbor] == -1:  # 방문 x 이면
                q.append(neighbor)
                distance[neighbor] = distance[cur] + 1


# 최단 거리가 k인 모든 도시의 번호 출력
bfs(x)

has_result = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        has_result = True
if not has_result:
    print(-1)

# [2번 : 시간초과]
# if distance.count(k) == 0:
#     print(-1)
# else:
#     for i in range(n + 1):
#         if distance[i] == k:
#             print(i)

# [1번 : 시간초과]
# result = list(filter(lambda i: distance[i] == k, range(1, n + 1)))
# if result:
#     print("\n".join(map(str, result)))
# else:
#     print(-1)
