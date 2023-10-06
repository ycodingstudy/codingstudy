# 공유기 설치 : https://www.acmicpc.net/problem/2110

# 집 N개가 수직선 위에 있음. 딱 C개의 공유기를 설치하려고 함
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
# -> 가장 인접한 두 공유기 사이의 최대 거리 구하기 (let 구하고자 하는 것 mid)
import sys
input = sys.stdin.readline()

def check(mid, homes, c):
    # mid : 가장 인접한 두 공유기 사이의 최대 거리
    # 무엇을 목적으로 하는 함수여야 할까? -> mid를 유지하면서 집을 설치할 수 있는가? == hint
    cnt = 1 # 1번집
    last_install = homes[0]
    for home in homes[1:]:
        if home - last_install >= mid: # mid값 이상으로 설치가 가능하면
            cnt += 1 # 설치 체크
            last_install = home # 마지막 위치 갱신
    return cnt >= c # mid만 보장된다면 몇개가 설치되건 상관 없는 점을 고려

def bi_search_iter(homes, start, end, c):
    res = -1
    while start <= end:
        mid = (start + end) // 2 # mid : 가장 인접한 두 공유기 사이의 최대 길이
        if check(mid, homes, c): # 가능하다면
            res = max(res, mid)
            start = mid + 1 # right(더 크게 해볼까?)
        else:
            end = mid - 1 # left
    return res

n, c = map(int, input().split())
homes = []
for _ in range(n):
    homes.append(int(input()))
homes.sort()
# start와 end에 무엇을 넣을까? -> 가능한 값의 min과 max
print(bi_search_iter(homes, 1, homes[-1] - homes[0], c))
