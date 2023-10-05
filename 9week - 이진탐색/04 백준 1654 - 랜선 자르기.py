# https://www.acmicpc.net/problem/1654

def check(limit, arr, n):
    # 목적 : limit의 크기로 arr을 나누어서 n개를 만들 수 있는가
    if limit == 0:
        return False # zero division error
    for a in arr:
        n = n - (a // limit)
    return n <= 0 # n개보다 많이 만드는 것도 n에 포함 됨


def bi_search_iter(arr, start, end, n):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if check(mid, arr, n): # mid라는 길이가 가능하면 더 늘려보자
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

# k개의 길이가 다른 랜선을 잘라서 길이가 같은 n개의 랜선으로 만들 때 n의 최대 길이
k, n = map(int, input().split())
origin = []
for _ in range(k):
    origin.append(int(input()))

origin.sort()
print(bi_search_iter(origin, 1, origin[-1], n)) # zero division error






