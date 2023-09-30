import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
card = PriorityQueue()
for _ in range(n):
    card.put(int(sys.stdin.readline()))

result = 0
for i in range(n - 1):
    a = card.get()
    b = card.get()
    tmp = a + b
    card.put(tmp)
    result += a + b


print(result)
