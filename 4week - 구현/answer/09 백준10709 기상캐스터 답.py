H, W = map(int, input().split())

res = []
for _ in range(H):
    s = input()
    li = [] # 한 줄에 대한 결과물
    c_idx = -1
    for i in range(W):
        if s[i] == 'c': # 처음 cloud가 있는 경우
            li.append(0) # 0을 넣고
            c_idx = i # 한 줄에 대한 c_idx를 업데이트
        elif c_idx == -1: # c_idx가 -1인 경우(구름이 올리 없는 경우)
            li.append(-1) # -1을 넣음
        else: # 이전에 업데이트된 c_idx가 존재하는 경우
            li.append(i - c_idx) # 현재와 그 구름까지의 거리
    res.append(li) # 한 줄에 대한 결과물을 넣어줌

for a in res:
    print(*a)
