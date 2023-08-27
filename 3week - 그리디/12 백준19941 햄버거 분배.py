# 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.

# 식탁의 길이 N,
# 햄버거를 선택할 수 있는 거리 K,
# 사람과 햄버거의 위치
# 햄버거를 먹을 수 있는 최대 사람의 수
n, k = map(int, input().split())
tables = list(input())

cnt = 0
for i in range(n):
    if tables[i] == 'P':
        left = i - k if i - k >= 0 else 0
        right = i + k if i + k < n else n - 1
        for j in range(left, right + 1):
            if tables[j] == 'H':
                tables[j] = 0
                cnt += 1
                break
print(cnt)

# ========== 시간 초과 =============
# n, k = map(int, input().split())  # 20, 1
# tables = input()
#
# buggers = []
# people = []
# for i in range(n): # O(n)
#     if tables[i] == 'H':
#         buggers.append(i)
#     else:  # 'P'
#         people.append(i)
#
# cnt = 0
# for person in people:
#     left = person - k
#     right = person + k
#
#     for bugger in buggers:
#         if left <= bugger <= right:
#             buggers.remove(bugger)
#             cnt += 1
#             break
#
# print(cnt)
