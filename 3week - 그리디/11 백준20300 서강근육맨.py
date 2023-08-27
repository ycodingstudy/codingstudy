# 1번 PT를 받을 때 2개의 기구를 사용
# 마지막에 한 개의 기구가 남을 때는 하나만 사용
# PT를 한 번 받을 때 근 손실의 정도가 M을 넘지 않게 함

# 운동 기구 두 개를 사용해서 PT를 받을 때
# 근손실 정도는 두 운동 기구의 근손실 정도의 합
# 최소의 M값(근손실 정도 최소로)
from itertools import combinations

n = int(input())  # 운동 기구의 개수
muscle_loss = list(map(int, input().split()))

if n % 2 == 0:  # 1 2 3 4 5 6
    muscle_loss.sort()  # 1 2 3 4 5 6
    all_sum = []
    for i in range(n // 2):  # 3 -> index 0, 1, 2까지 접근
        sum = muscle_loss[i] + muscle_loss[-1 - i]
        all_sum.append(sum)
    print(max(all_sum))
else:  # 1 2 3 4 5
    muscle_loss.sort()  # 1 2 3 4 5
    all_sum = []
    for i in range(n // 2):  # 0 ,1 까지 접근
        sum = muscle_loss[i] + muscle_loss[-2 - i]
        all_sum.append(sum)
    all_sum.append(muscle_loss[-1])
    print(max(all_sum))

# 7
# 3 5 7 12 9 8 1
# 1 3 5 7 8 9 /12
# 1 9 / 3 8 / 5 7 /12
