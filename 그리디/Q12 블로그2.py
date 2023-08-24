# https://www.acmicpc.net/problem/20365
# 8
# BBRBRBBR
N = int(input())
target = list(input())
cnt = 0
for i in target:
    cnt = cnt-1 if i == "B" else cnt+1

bColor = "B" if cnt < 0 else "R"
cnt = 1
before = bColor
for now in target:
    # 만약 색을 칠해야 하면
    cnt = cnt+1 if now != bColor and now != before else cnt
    before = now

print(cnt)

