n = 12  # 외벽의 길이
weak = [1, 5, 6, 10]  # 취약 지점의 위치
dist = [1, 2, 3, 4]  # 각 친구들이 1시간 당 이동 가능 거리


# result : 필요한 최소 친구 수, # 전부 투입해도 불가능 하면 -1을 return
from itertools import combinations

def solution(n, weak, dist):
    wall = [0] * n
    for i in weak:
        wall[i] = -1

    dist.sort(reverse=True)








print(solution(n, weak, dist))
