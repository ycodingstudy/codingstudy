from itertools import combinations

n, m = map(int, input().split())

# 집과 치킨집의 좌표 담기
home = []
chicken = []

# 맵 만들기
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# 집과 치킨집의 좌표를 담음
for row in range(n):
    for col in range(n):
        if board[row][col] == 1:
            home.append([row, col])
        elif board[row][col] == 2:
            chicken.append([row, col])
        else:
            continue

if m == len(chicken):
    chicken_distance = []
    for h in home:
        tmp = []  # 1개의 집과 m개의 치킨집의 개별 치킨 거리
        for c in chicken:
            distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
            tmp.append(distance)
        min_distance = min(tmp)  # 1개의 집의 최소 치킨거리
        chicken_distance.append(min_distance)  # 각 집들에 대한 치킨거리
    print(sum(chicken_distance))
else:

    chicken_idx = [i for i in range(len(chicken))]

    combs = list(combinations(chicken_idx, m))  # [(0, 1), (0,2), ... ]

    all_chicken_distance = [] # 전체 조합에 대한 동네 치킨 거리 (조합별 각 집들에 대한 치킨 거리의 합)
    for comb in combs: # chicken집 좌표에 접근하기 위한 index 조합. comb : (0,1)
        chicken_distance = []
        for h in home:
            tmp = [] # 1개의 집에 대한 m개의 치킨집 거리
            for i in range(m):
                c = chicken[comb[i]]
                distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
                tmp.append(distance)
            min_distance = min(tmp) # 1개의 집에 대한 치킨거리
            chicken_distance.append(min_distance) # 각 집들에 대한 치킨거리
        all_chicken_distance.append(sum(chicken_distance))

    print(min(all_chicken_distance))
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
# 답은 5

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2
# 답은 10

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 답은 11
