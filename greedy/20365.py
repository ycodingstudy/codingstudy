# import sys
# n = int(sys.stdin.readline())
# s = list(sys.stdin.readline().rstrip())
#
#
# if s.count('B') >= s.count('R'):
#     main_color = 'B'
# else:
#     main_color = 'R'
#
# main_color = 'B'
# cnt = 1 # 메인컬러를 정하면서 1회의 색칠을 사용함
#
# i = 0
# while i < n:
#     if s[i] != main_color:
#         s[i] = main_color # 메인컬러 아니면 메인컬러로 바꿔놓음
#         cnt += 1
#
#         while True:
#             i += 1
#             if i >= n or s[i] == main_color :
#                 break
#
#             if s[i] != main_color:
#                 s[i] == main_color
#
#     i += 1
#
# print(cnt)

import sys
input = sys.stdin.readline

n = int(input())
s = input()

colors = { 'B' : 0, 'R' : 0 } #딕셔너리
colors[s[0]] +=1 #처음 색깔 칠하기
for i in range(1, n): #다른 색이 나오면 해당 색깔 칠하는 횟수 +1
    if s[i] != s[i-1]:
        colors[s[i]]+=1

result = min(colors['B'], colors['R'])+1 #칠할 횟수가 더 많은 것을 먼저 전체 칠하고(1) 칠할 횟수가 더 적은 것의 횟수 값(min)을 더한다.
print(result)