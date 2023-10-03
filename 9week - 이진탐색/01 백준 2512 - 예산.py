# https://www.acmicpc.net/problem/2512

# 정해진 총액 이하에서 가능한 최대의 총 예산 배정
# 모든 요청 가능 -> 그대로
#          불가능 -> 특정 정수 상한액 계산 후, 이상이면 상한액으로

# 전체 국가 예산 485
# 120 110 140 150
# 상한액찾기! -> 127

n = int(input())  # 지방의 수
request = list(map(int, input().split()))
budget = int(input())

request.sort()  # [110, 120, 140, 150]

def can_allocate(limit):
    # 중앙값이 할당 가능한지 확인
    allocation = 0
    for req in request:
        if req <= limit:  # 할당 가능 상태
            allocation += req  # 할당
        else:
            allocation += limit  # 상한 할당
    return allocation <= budget  # 전체 할당이 예산 이하면 할당 가능


def bi_search_recursion(start, end): # index가 아니라 value가 들어감
    if start > end:
        return start - 1 # 이전 상황으로 복귀해서 return
    mid = (start + end) // 2 # 0과 150 -> mid : 75
    if can_allocate(mid):  # 예산을 늘려감
        return bi_search_recursion(mid + 1, end) # 76과 150 -> mid = 113 -> # 113과 150 -> mid = 131
    else:  # 예산을 줄여감
        return bi_search_recursion(start, mid - 1) # 113과 130 -> mid = 121


if sum(request) <= budget:
    print(request[-1])
else:
    res = bi_search_recursion(0, request[-1]) # request[0]가 아니라 0을 넣어야함
    print(res)
