# from itertools import combinations

n = int(input())  # 필요한 에너지 드링크의 수
drinks = list(map(int, input().split()))  # 각 에너지 드링크의 양

drinks.sort(reverse=True)  # [10, 9, 6, 3, 2]
quantity = drinks[0]
for i in range(1, len(drinks)):
    quantity += drinks[i] / 2

# 20.0이면 20으로 변경하고 761.5이면 그대로 출력
if quantity == int(quantity):
    print(int(quantity))
else:
    print(quantity)
