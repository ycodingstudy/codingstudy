import sys
n, c = map(int, sys.stdin.readline().split())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

start = 1 # 모든 집은 다른 좌표에 있으므로 최소 공유기 거리는 1
end = lst[-1] - lst[0] # 집 사이의 최대 거리
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = lst[0]
    count = 1 # 항상 1번째 집에 공유기를 설치

    for i in range(1, n):
        if lst[i] - cur >= mid:
            count += 1
            cur = lst[i]

    if count >= c:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)



