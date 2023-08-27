n = int(input())  # 색칠해야하는 문제의 수
colors = input()  # BBRBRBBR

# index
blue_idx = []
red_idx = []
for i in range(n):
    if colors[i] == 'B':
        blue_idx.append(i)
    else:  # 'R'
        red_idx.append(i)

res = [0] * n
cnt = 0

if n != 1:
    blue_distance = blue_idx[-1] - blue_idx[0] if len(blue_idx) != 0 else 0
    red_distance = red_idx[-1] - red_idx[0] if len(red_idx) != 0 else 0
    if blue_distance > red_distance:
        for i in range(blue_idx[0], blue_idx[-1] + 1):
            res[i] = 'B'
        cnt += 1

        while True:
            if len(red_idx) == 0:
                break

            left, right = 0, 0

            for i in range(len(red_idx) - 1):
                if red_idx[i + 1] - red_idx[i] == 1:
                    right += 1
                else:
                    break

            for i in range(left, right + 1):
                res[red_idx[i]] = 'R'
            cnt += 1
            del red_idx[left:right + 1]
            # print(cnt)
            # print("ress : ", res)
    else:
        for i in range(blue_idx[0], blue_idx[-1] + 1):
            res[i] = 'R'
        cnt += 1

        while True:
            if len(blue_idx) == 0:
                break

            left, right = 0, 0

            for i in range(len(blue_idx) - 1):
                if blue_idx[i + 1] - blue_idx[i] == 1:
                    right += 1
                else:
                    break

            for i in range(left, right + 1):
                res[blue_idx[i]] = 'R'
            cnt += 1
            del blue_idx[left:right + 1]
            # print(cnt)
            # print("ress : ", res)
else:
    cnt = 1


# print("res : ", res)
print(cnt)
