# https://www.acmicpc.net/problem/6236
# n일간 자신이 사용할 금액, m번만 돈을 인출
# 돈이 남으면 집어 넣고, 부족하면 집어 넣은 후 k원 인출
# k : 하루 인출 금액(최소화)

def check(limit, use_plan, m):
    # 목표 : limit만큼 돈을 m번 인출 성공하면 True
    cur_money = 0 # 현재 꺼낸 돈
    for today_use in use_plan:
        if today_use > limit:
            return False
        if today_use <= cur_money:
            cur_money -= today_use
        else: # 꺼낸 돈이 쓸 돈 보다 부족하면
            m -= 1
            if m < 0:
                return False
            cur_money = limit - today_use #  돈 집어 넣은 것(limit) - today_use
    return True


def bi_search_recursion(use_plan, start, end, m):
    if start > end:
        return start  # mid 값을 반환해야함
    mid = (start + end) // 2
    if check(mid, use_plan, m):
        # 더 적은 금액 찾기
        return bi_search_recursion(use_plan, start, mid - 1, m)
    else:
        return bi_search_recursion(use_plan, mid + 1, end, m)

def bi_search_iter(use_plan, start, end, m):
    res = 0
    while start <= end:
        mid = (start + end)//2
        if check(mid, use_plan, m):
            res = mid
            end = mid - 1 # 아래쪽 보기
        else:
            start = mid + 1
    return res

n, m = map(int, input().split())
use_plan = []
for _ in range(n):
    use_plan.append(int(input()))

# print(bi_search_recursion(use_plan, 1, sum(use_plan), m))
print(bi_search_iter(use_plan, max(use_plan), sum(use_plan), m)) # 왜 sum

# 만약 use_plan = [2000, 2000, 2000, 2000, 2000]이고, m = 1이라고 가정해봅시다.
# max(use_plan)이 2000이지만, 정답은 10000입니다. 왜냐하면 현우는 한 번의 인출로 5일 동안의 사용 금액을 충당해야 하기 때문입니다.
# 이러한 예외적인 경우를 고려하지 않으면, 이진 탐색 알고리즘이 정확한 결과를 반환하지 못할 것입니다.