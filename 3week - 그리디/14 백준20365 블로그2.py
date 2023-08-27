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
cnt = 1

if n != 1:
    blue_distance = blue_idx[-1] - blue_idx[0] if len(blue_idx) != 0 else 0
    red_distance = red_idx[-1] - red_idx[0] if len(red_idx) != 0 else 0
    if blue_distance > red_distance:
        while len(red_idx) != 0:

            left, right = 0, 0

            for i in range(len(red_idx) - 1):
                if red_idx[i + 1] - red_idx[i] == 1:
                    right += 1
                else:
                    break

            cnt += 1
            del red_idx[left:right + 1]
    else:
        while len(blue_idx) != 0:

            left, right = 0, 0

            for i in range(len(blue_idx) - 1):
                if blue_idx[i + 1] - blue_idx[i] == 1:
                    right += 1
                else:
                    break
            cnt += 1
            del blue_idx[left:right + 1]

print(cnt)

# 1:07:20 소요