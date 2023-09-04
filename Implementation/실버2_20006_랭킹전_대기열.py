import sys

START = 'Started!'
WAITING = 'Waiting!'

p, m = map(int, input().split())

lst = []
#lst = [[[1000, 'test']]] # 임시로 하나 데이터 넣어둠
for i in range(p):
    player_num, player_str = list(sys.stdin.readline().rstrip().split())
    player_num = int(player_num)

    flag = 0 #방에 들어갔는지 안들어갔는지 체크
    for j in range(len(lst)): # 기존에 있는 방을 탐색
        if lst[j][0][0] - 10 <= player_num <= lst[j][0][0] + 10 and len(lst[j]) < m:
            lst[j].append([player_num, player_str])
            flag = 1
            break

    if flag == 0: # 방이 없다면 새로 만듬
        lst.append([[player_num, player_str]])

#lst.pop(0)

for i in range(len(lst)):
    lst[i].sort(key=lambda x: x[1])
    if len(lst[i]) == m:
        print(START)
    else:
        print(WAITING)
    for j in range(len(lst[i])):
        print(lst[i][j][0], lst[i][j][1])
