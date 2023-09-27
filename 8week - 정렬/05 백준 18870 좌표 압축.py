# https://www.acmicpc.net/problem/18870

n = int(input())
origin = list(map(int, input().split())) # [2, 4, -10, -4, -9]

del_duple = sorted(set(origin)) # {2, 4, -10, -9} -> [-10, -9, 2, 4]
dic = {}
for i, num in enumerate(del_duple): # 정렬되었기 때문에 자기 index만큼 작은 값 가짐
    dic[num] = i

for i, num in enumerate(origin): # origin 업데이트
    origin[i] = dic[num]

print(*origin)
