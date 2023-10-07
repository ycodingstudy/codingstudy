import sys

n = int(sys.stdin.readline())
budget_lst = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

start = 0
end = max(budget_lst)

while start <= end:
    print('start: ', start)
    print('mid: ', end)
    mid = (start + end) // 2
    total = 0  # 총 지출 양
    for budget in budget_lst:
        if budget > mid:
            total += mid
        else:
            total += budget

    if total <= target:
        start = mid + 1
    else:
        end = mid - 1
    print('------후--------')
    print('start: ', start)
    print('mid: ', end)
    print('-------------')

print(end)
