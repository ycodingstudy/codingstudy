# key : [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock : [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]  # len(key)는 3이 나옴
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def turn_right(key):
    # M x M
    m = len(key)
    new_key = []
    for col in range(m):
        new_row = []
        for row in range(m - 1, -1, -1):
            new_row.append(key[row][col])
        new_key.append(new_row)
    # print(new_key)
    return new_key


def is_success(board, start_idx, last_idx):
    for row in range(start_idx, last_idx + 1):
        for col in range(start_idx, last_idx + 1):
            if board[row][col] == 0 or board[row][col] == 2:
                return False
    return True


def init_board(n, m, lock):
    start_idx = m - 1

    new_board = [[0] * (n + m + 1) for _ in range(n + m + 1)]
    for row in range(n):
        for col in range(n):
            new_board[start_idx + row][start_idx + col] = lock[row][col]
    return new_board


def solution(key, lock):
    n = len(lock)
    m = len(key)

    start_idx = m - 1
    last_idx = start_idx + n - 1

    board = init_board(n, m, lock)

    # board 한 변 길이 - key 길이
    for x in range(0, len(board) - m + 1):
        for y in range(0, len(board) - m + 1):

            for rotation in range(4):  # 한 자리에서 회전 체크
                for i in range(m):
                    for j in range(m):  # key를 더해
                        board[x + i][y + j] += key[i][j]
                if is_success(board, start_idx, last_idx): # 해당 부분만 검사하고 싶다.
                    return True
                board = init_board(n, m, lock)
                key = turn_right(key)

    return False


print(solution(key, lock))

# def turn_right(key):
#     # M x M
#     m = len(key)
#     new_key = []
#     for col in range(m):
#         new_row = []
#         for row in range(m - 1, -1, -1):
#             new_row.append(key[row][col])
#         new_key.append(new_row)
#     # print(new_key)
#     return new_key
#
#
# def is_success(mat):
#     m = len(mat)
#     for row in range(m):
#         if mat[row].count(2) > 0 or mat[row].count(0) > 0:
#             return False
#     return True


# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#
#     for x in range(0, n - m + 1):
#         for y in range(0, n - m + 1):  # 이동
#
#             for rotation in range(4):  # 한 자리에서 회전 체크
#                 mat = [[0] * m for i in range(m)]
#                 for i in range(m):
#                     for j in range(m):
#                         mat[i][j] = key[i][j] + lock[x + i][y + j]
#
#                 if is_success(mat): return True
#
#                 key = turn_right(key)
#
#     return False
