import heapq

n = int(input())
cards = []

for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0
if len(cards) == 1:
    print(result)
else:
    for i in range(n-1):
        prev = heapq.heappop(cards)
        cur = heapq.heappop(cards)
        temp = prev+ cur
        result+= temp
        heapq.heappush(cards, temp)
    print(result)