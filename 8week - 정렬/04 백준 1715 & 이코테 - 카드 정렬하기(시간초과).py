n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

cards.sort() # [10, 20, 40]

total = 0
for i in range(1, n): # i : 1       / i : 2
    for j in range(i + 1): #  j : 0 / j : 0, 1
        total += cards[j]

print(total)
