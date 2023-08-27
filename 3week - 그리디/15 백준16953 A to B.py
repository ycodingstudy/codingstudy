# 0827(3주차) 때, 풀이를 이미 봤지만..
# 생각처럼 구현할 수 있을 지 확인용
a, b = map(int, input().split())

cnt = 1
while b != a: # 두 값이 동일해지면 탈출
    cnt += 1
    tmp = b # 현재의 b 값을 담아둠
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if tmp == b: # 1을 제거하는 연산과 2를 나누는 연산 둘 다 불가하면 탈출
        print(-1)
        break
else:
    print(cnt)