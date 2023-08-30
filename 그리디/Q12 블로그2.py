# https://www.acmicpc.net/problem/20365
# 8
# BBRBRBBR
N = int(input())
target = list(input())
cnt = 0
for i in target:
    #더 많은 개수를 차지하는 그룹 고르기
    cnt = cnt-1 if i == "B" else cnt+1

bColor = "B" if cnt < 0 else "R"  #더 많은 개수의 컬러 고르기
cnt = 1
before = bColor
for now in target:
    # 만약 처음 고른 컬러와 현재가 다르면서, 이전 컬러와 다른 색인 경우 cnt+1
    cnt = cnt+1 if now != bColor and now != before else cnt
    before = now

print(cnt)

N = int(input())
target = list(input())
cnt = 0







bColor = target[0]
cnt = 0
before = bColor
for now in target:
    # 만약 처음 고른 컬러와 현재가 다르면서, 이전 컬러와 다른 색인 경우 cnt+1
    cnt = cnt+1 if now != bColor and now != before else cnt
    before = now

print(cnt + 1)