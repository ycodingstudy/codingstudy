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
        if lst[j] != 0 :
            virus_coordinate.append([i, j])
    graph.append(lst)

s, x, y = map(int, sys.stdin.readline().split())

def bfs(num):
    queue = deque(virus_coordinate)

    i = 0
    while True:

        for i in range(len(virus_coordinate)):

            tmp_x, tmp_y = queue.popleft()
            for i in range(4):
                target_x = dx[i]
                target_y = dy[i]

                if target_x < 0 or target_x >= n or target_y < 0 or target_y >=k :
                    pass

                elif graph[target_x][target_y] == 0:
                    graph[target_x][target_y] = graph[tmp_x][tmp_y]
                    queue.append([target_x, target_y])

bfs(s)