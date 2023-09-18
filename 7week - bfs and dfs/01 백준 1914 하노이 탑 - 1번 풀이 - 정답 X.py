# k : 원판의 수, fr : from, tmp : 중간 장소, to : 목적지
def hanoi(k, fr, tmp, to, flag):
    cnt = 0
    if k == 1:
        if flag:
            print(fr, to)
        cnt += 1
        return cnt
    # 마지막 원판 1개를 제외한, 나머지를 fr에서 to를 거쳐 tmp로 이동
    cnt += hanoi(k-1, fr, to, tmp, flag)
    # 마지막 원판 1개를, 목적지(to)로 바로 이동
    cnt += 1
    if flag:
        print(fr, to)
    # tmp로 옮긴 k-1개를 to로 옮기기
    cnt += hanoi(k-1, tmp, fr, to, flag)
    return cnt

n = int(input())
flag = True if n <= 20 else False
print(hanoi(n, 1, 2, 3, flag))