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













n = int(input())
def hanoi(n, start, to , via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

print(2**n-1)
if n <= 20:
    hanoi(n, 1, 3, 2)
