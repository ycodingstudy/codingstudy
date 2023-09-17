from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 이동 가능한 위치들
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = (
            pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i])
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위로 회전하거나, 아래로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 다음 위치들을 반환
    return next_pos


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # bfs
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while 1:
        pos, cost = q.popleft()
        # (n, n)에 도달했다면 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

