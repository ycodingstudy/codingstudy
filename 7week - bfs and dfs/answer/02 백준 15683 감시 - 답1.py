# https://www.acmicpc.net/problem/15683
from collections import deque
import copy


def get_min_cnt(board):
    cnt = 0
    for b in board:
        cnt += b.count(0)
    return cnt


def monitor(x, y, i, board):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            break
        if board[nx][ny] == 6:
            break
        if board[nx][ny] == '#' or board[nx][ny] == 0:
            board[nx][ny] = '#'
        x, y = nx, ny

def get_cctv_directions(cctv_kind):
    directions = []
    if cctv_kind == 1:
        directions = [[0], [1], [2], [3]]
    elif cctv_kind == 2:
        directions = [[0, 1], [2, 3]]
    elif cctv_kind == 3:
        directions = [[0, 3], [3, 1], [1, 2], [2, 0]]
    elif cctv_kind == 4:
        directions = [[0, 1, 3], [1, 2, 3], [2, 0, 3], [0, 1, 2]]
    else:
        directions = [[0, 1, 2, 3]]
    return directions



n, m = map(int, input().split())
board = []
cctvs = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        tmp = board[i][j] # tmp : cctv의 종류 or 6이면 벽
        if 1<= tmp <= 5:
            cctvs.append((i, j, tmp))

def dfs(cctv_idx, board):
    if cctv_idx == len(cctvs):
        return get_min_cnt(board)

    x, y, cctv_kind = cctvs[cctv_idx]

    min_val = float('inf')
    directions = get_cctv_directions(cctv_kind) #  1 : [[0], [1], [2], [3]]
    for direction in directions:
        new_board = copy.deepcopy(board)
        for d in direction:
            monitor(x, y, d, new_board)
        min_val = min(min_val, dfs(cctv_idx+1, new_board))

    return min_val

res = dfs(0, board)
print(res)