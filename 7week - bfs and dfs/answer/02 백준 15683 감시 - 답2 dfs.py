import copy

n, m = map(int, input().split())
cctv = []
graph = []
mode = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])


def fill(board, mm, x, y):  # see하는 함수
    for i in mm:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7


def dfs(depth, arr):  # arr : graph
    global min_val

    if depth == len(cctv):
        count = 0  # 감시 되지 않은 영역을 세는 곳
        for i in range(n):
            count += arr[i].count(0)
        min_val = min(min_val, count)
        return

    tmp = copy.deepcopy(arr)  # board(map)을 복사함
    cctv_num, x, y = cctv[depth]  # depth에 따라 cctv를 꺼내옴
    for i in mode[cctv_num]: # 현재의 cctv를 회전함
        fill(tmp, i, x, y)  # 감시를 쭉 하고
        dfs(depth + 1, tmp)  # 한 번 더 들어감
        tmp = copy.deepcopy(tmp)  # backtracking 맵을 돌림


min_val = int(1e9)
dfs(0, graph)
print(min_val)
