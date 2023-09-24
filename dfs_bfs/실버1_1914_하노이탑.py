# MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"
#
#
# def move(N, start, to):
#     print(MSG_FORMAT.format(N, start, to))
#
# def hanoi(N, start, to, via):
#     if N == 1:
#         move(1, start, to)
#     else:
#         hanoi(N-1, start, via, to)
#         move(N, start, to)
#         hanoi(N-1, via, to, start)
#
# hanoi(5, 'A', 'C', 'B')











# 이 문제의 핵심
# 1. n - 1개의 원판을 3번을 통해 2번으로 옮기기
# 2. 맨 아래 원판을 3번 으로 옮기기
# 3. 2번에 옮겼던 n - 1 개의 원판을 다시 3번 원판 으로 옮기기

n = int(input())
def hanoi(n, start, to , via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to) # n - 1개 원판 2번으로 옮기기
        print(start, to) # 맨 아래 원판 옮기기
        hanoi(n-1, via, to, start) # 2번에 있던 원판 3번으로 옮기기

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)
