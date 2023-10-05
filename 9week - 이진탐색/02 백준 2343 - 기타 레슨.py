# https://www.acmicpc.net/problem/2343

# 블루레이에 총 n개의 강의가 들어감. i강의와 j 강의를 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화

def can_allocate(limit, lectures, b_cnt):
    cur_sum = 0
    for lecture in lectures:
        if lecture > limit: # 최대길이(limit)보다 강의가 큰 경우
            return False
        elif cur_sum + lecture > limit: # 기존 합계 + 새로운 강의 > limit
            if b_cnt == 1: # 공간없음 -> 그런데 마지막 블루레이에 도달했음
                return False
            b_cnt -= 1 # blue ray 사용
            cur_sum = lecture # 현재의 강의로 해야함
        else:
            cur_sum += lecture
    return True

def bi_search_iter(start_val, end_val, lectures, b_cnt):
    res = 0
    while start_val <= end_val:
        mid = (start_val + end_val) // 2
        if can_allocate(mid, lectures, b_cnt): # 할당이 가능하면 -> 최소를 찾기 위해 줄인다
            res = mid
            end_val = mid - 1 # left를 찾아야해
        else:
            start_val = mid + 1 # right를 찾아야해
    return res

# 블루레이에 총 n개의 강의가 들어감.
# m개의 블루레이에 모든 기타 강의를 녹화할 때 최소(최소에서 올려가기)
n, m = map(int, input().split())
lectures = list(map(int, input().split())) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# m개의 블루레이에 limit 길이만큼 모두 담아야해
print(bi_search_iter(min(lectures), sum(lectures), lectures, m))











