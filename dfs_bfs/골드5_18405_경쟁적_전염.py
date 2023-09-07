import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

graph = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

virus_coordinate = []
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in range(len(lst)):
        if lst[j] != 0:
            virus_coordinate.append([i, j, lst[j]]) # 바이러스 좌표 + 값을 넣어줌
    graph.append(lst)


virus_coordinate.sort(key=lambda x: x[2])
for i in range(len(virus_coordinate)):
    virus_coordinate[i].pop()


s, x, y = map(int, sys.stdin.readline().split())
def bfs(num):
    queue = deque(virus_coordinate)

    for second in range(num): # 1초 2초 이런식으로 초를 세주기위해서
        cycle = len(queue) # 계속 queue의 길이를 업데이트해줌.(큐 안에는 좌표가 들어있음)

        for r in range(cycle): # 큐의 길이만큼 반복하도록 지정.
            tmp_x, tmp_y = queue.popleft()
            for i in range(4):
                target_x = tmp_x + dx[i]
                target_y = tmp_y + dy[i]

                if target_x < 0 or target_x > (n - 1) or target_y < 0 or target_y > (k - 1) :
                    continue

                elif graph[target_x][target_y] == 0:
                    graph[target_x][target_y] = graph[tmp_x][tmp_y]
                    queue.append([target_x, target_y])


bfs(s)

print(graph[x-1][y-1])