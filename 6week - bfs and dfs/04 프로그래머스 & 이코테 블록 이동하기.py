def turn(board, robot):
    robot


def dfs(board, robot):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(board)
    cnt = 0
    if board[n - 1][n - 1] == 2:
        return cnt

    x1, y1 = robot[0][0], robot[0][1]
    x2, y2 = robot[1][0], robot[1][1]
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        # 범위 내에 있으면서
        if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
            # 벽을 닿지 않고 이전에 방문한 곳이 아닐 때
            if board[nx1][ny1] != 1 and board[nx2][ny2] != 1 and board[nx1][ny1] != 2 and board[nx2][ny2] != 2:
                board[x1][y1] = board[x2][y2] = 0 # 기존의 것을 지난 처리
                board[nx1][ny1] = board[nx2][ny2] = 2 # 새로운 위치로 이동
                cnt += 1 # 이동(1초 증가)
                robot[0][0], robot[0][1] = nx1, ny1
                robot[1][0], robot[1][1] = nx2, ny2
                dfs(board, robot)

    # 4 방향을 다 갈 수 없다면, 회전
    turn(board, robot)
    cnt += 1
    dfs(board, robot)


def solution(board):
    answer = 0
    n = len(board)  # 5가 나오겠지만 index는 1부터 6까지
    board[0][0] = board[0][1] = 2  # 로봇이 있는 곳은 0으로 표시

    return answer


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
