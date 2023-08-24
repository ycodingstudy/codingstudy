
N = int(input())
target = input()

# 첫 번째 그룹의 색과 전환 횟수 초기화
first_color = target[0]
switch_count = 0

# 연속된 그룹 전환 횟수 계산
for i in range(1, N):
    if target[i] != first_color and target[i] != target[i - 1]:
        switch_count += 1

print(switch_count + 1)  # 마지막 그룹을 더해줌