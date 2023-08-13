import sys

s = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

tmp_len = 0
cnt = 0
result = 0

#ababababa
#aba
while True:
    result = s.find(target, tmp_len) # 0
    tmp_len = result + len(target) # 0 + 3

    if result != -1:
        cnt += 1

    else:
        break

print(cnt)

