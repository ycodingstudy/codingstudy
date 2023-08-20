board = list(input())
dot_index = []
res = ""

for i in range(len(board)):
    if board[i] == ".":
        dot_index.append(i)
dot_index.append(len(board))  # board의 길이 추가

if len(dot_index) > 1:
    for i in range(len(dot_index)):
        if i == 0:
            aaaa_cnt = dot_index[i] // 4
            after_aaaa = dot_index[i] % 4

            bb_cnt = after_aaaa // 2
            after_bb = after_aaaa % 2

            if after_bb != 0:
                res = -1
                break
            else:
                res = res + "AAAA" * aaaa_cnt + "BB" * bb_cnt + "."
        else:
            aaaa_cnt = (dot_index[i] - dot_index[i - 1] - 1) // 4
            after_aaaa = (dot_index[i] - dot_index[i - 1] - 1) % 4

            bb_cnt = after_aaaa // 2
            after_bb = after_aaaa % 2
            if after_bb != 0:
                res = -1
                break

            if i == len(dot_index) - 1:
                res = res + "AAAA" * aaaa_cnt + "BB" * bb_cnt
            else:
                res = res + "AAAA" * aaaa_cnt + "BB" * bb_cnt + "."

    print(res)

else:  # board에 .이 존재하지 않는 경우
    length = len(board)

    aaaa_cnt = len(board) // 4
    after_aaaa = length % 4

    bb_cnt = after_aaaa // 2
    after_bb = after_aaaa % 2

    if after_bb != 0:
        res = "-1"
    else:
        res = "AAAA" * aaaa_cnt + "BB" * bb_cnt

    print(res)
