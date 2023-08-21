# https://velog.io/@tunaman95/%EB%B0%B1%EC%A4%80-20300%EB%B2%88-%EC%84%9C%EA%B0%95%EA%B7%BC%EC%9C%A1%EB%A7%A8-Python

import sys

input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
l.sort()

m = -int(1e9)  # 극단적으로 작은 수를 넣어 주고
if n % 2 == 0:
    for i in range(n // 2):
        m = max(l[i] + l[n - i - 1], m)  # 매번 업데이트 해주는 방식
else:
    for i in range((n - 1) // 2):
        m = max(l[i] + l[n - i - 2], m)
    print(max(m, l[-1]))
