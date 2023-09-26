import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

cnt = 0
while len(cards) > 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    heapq.heappush(cards, first + second)
    cnt = cnt + first + second
print(cnt)
