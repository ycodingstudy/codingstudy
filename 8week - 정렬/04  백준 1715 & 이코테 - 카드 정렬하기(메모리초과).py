# 메모리 초과
n = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))

cards.sort()  # [10, 20, 40]

def together(array): # [10 ,20, 40]
    if len(array) <= 2:
        return sum(array)
    accumulation = array[0] + array[1] # 30
    new_array = [accumulation] + array[2:] # [30, 40]
    return accumulation + together(new_array) # 앞의 누적 값과 나머지 친구들


print(together(cards))
