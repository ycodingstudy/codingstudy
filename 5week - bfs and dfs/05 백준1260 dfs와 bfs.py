from collections import deque

n, m, v = map(int, input().split())  # 정점의 수, 간선의 수, 시작정점
graph = [[] for _ in range(n + 1)]  # 인덱스 보정
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for neighbors in graph:
    neighbors.sort()

visited_dfs = [False] * (n + 1)  # 인덱스 보정
visited_bfs = [False] * (n + 1)
res_dfs = []
res_bfs = []


def dfs(start):
    # 1) 방문 체크
    visited_dfs[start] = True
    res_dfs.append(start)
    # 2) 연결된 그래프 확인
    for node in graph[start]:
        # 3) 방문 안된 경우에 그 node에서 dfs
        if not visited_dfs[node]:
            dfs(node)

def bfs(start):
    # 1) 시작점을 넣고 방문 체크
    q = deque()
    q.append(start)
    visited_bfs[start] = True
    res_bfs.append(start)

    # 2) queue가 empty할 때까지 pop 시키며 주변 노드 확인
    while q:
        cur_node = q.popleft() # 현재노드 pop
        for neighbor in graph[cur_node]: # 그래프 상 현재 노드 이웃 노드
            if not visited_bfs[neighbor]: # 미방문시
                q.append(neighbor) # 처리
                visited_bfs[neighbor] = True
                res_bfs.append(neighbor)


dfs(v)
print(*res_dfs)
bfs(v)
print(*res_bfs)
