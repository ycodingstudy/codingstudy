from collections import deque

def is_valid(pos, board):
    n = len(board)
    return 0 <= pos[0] < n and 0 <= pos[1] < n and board[pos[0]][pos[1]] != 1


def get_next_pos(pos, board):
    next_pos = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i in range(4):
        pos_a = (pos[0][0] + dx[i], pos[0][1] + dy[i])
        pos_b = (pos[1][0] + dx[i], pos[1][1] + dy[i])
        if is_valid(pos_a, board) and is_valid(pos_b, board):
            next_pos.append((pos_a, pos_b))

    # 회전
    if pos[0][0] == pos[1][0]:  # 수평으로 위치할 때
        for i in [-1, 1]:  # 위, 아래로 이동
            if (is_valid((pos[0][0] + i, pos[0][1]), board)
                    and is_valid((pos[1][0] + i, pos[1][1]), board)):
                next_pos.append(((pos[0][0] + i, pos[0][1]), pos[0]))
                next_pos.append(((pos[1][0] + i, pos[1][1]), pos[1]))
    else:  # 수직으로 위치할 때
        for i in [-1, 1]:  # 좌, 우
            if (is_valid((pos[0][0], pos[0][1] + i), board)
                    and is_valid((pos[1][0], pos[1][1] + i), board)):
                next_pos.append((pos[0], (pos[0][0], pos[0][1] + i)))
                next_pos.append((pos[1], (pos[1][0], pos[1][1] + i)))

    return next_pos

def solution(board):
    n = len(board)
    visited = set()
    q = deque([((0, 0), (0, 1), 0)]) # robot의 초기 좌표와 거리
    visited.add(((0, 0), (0, 1)))

    while q:
        pos_a, pos_b, distance = q.popleft()
        if(pos_a == (n-1, n-1)) or (pos_b == (n-1, n-1)):
            return distance

        for next_pos in get_next_pos((pos_a, pos_b), board):
            if next_pos not in visited:
                q.append((*next_pos, distance + 1))
                visited.add(next_pos)
    return 0

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
print(solution(board))