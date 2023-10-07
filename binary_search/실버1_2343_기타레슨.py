import sys
# https://codingwonny.tistory.com/m/311 참고
n, m = map(int, input().split())
lecture_lst = list(map(int, sys.stdin.readline().split()))

start = max(lecture_lst)
end = sum(lecture_lst)

while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1
    for lecture in lecture_lst:
        if total + lecture > mid:
            count += 1
            total = 0
        total += lecture

    if count <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1


print(ans)

