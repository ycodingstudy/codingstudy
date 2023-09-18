def hanoi(k, fr, tmp, to, flag):
    if k == 1:
        if flag:
            print(fr, to)
        return

    # fr에서 to를 거쳐 tmp로 나머지를 전부 보냄
    hanoi(k - 1, fr, to, tmp, flag)
    # 마지막 원판을 목적지로 보냄
    if flag:
        print(fr, to)
    # tmp로 보내진 나머지 원판을 fr을 거쳐 to로 보냄
    hanoi(k - 1, tmp, fr, to, flag)


n = int(input())

print(2 ** n - 1)
flag = True if n <= 20 else False
hanoi(n, 1, 2, 3, flag)
