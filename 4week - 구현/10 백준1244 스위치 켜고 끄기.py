# 1 : 켜짐, 0 : 꺼짐
# n : 스위치 수,  스위치 번호 : 1 ~ n
# 남(1) : 스위치 번호 % 받은 수(n이하) == 0 -> 스위치 상태 바꿈
# 여(2) : 받은 수(n이하)의 번호 스위치 중심 좌우 대칭
#     + 가장 많은 스위치 포함 구간의 스위치를 모두 변경

n = int(input())

switches = list(map(int, input().split()))
switches.insert(0, -1)  # index 보정

num_of_students = int(input())
for _ in range(num_of_students):
    gender, switch_num = map(int, input().split())

    if gender == 1:
        # 전체를 다 돌지 않고 인덱스로 바로 가는 방법이 없을까?
        for i in range(switch_num, len(switches), switch_num):
            switches[i] = 1 - switches[i]
    else:  # gender == 2:
        left = right = switch_num  # 바꿀 스위치 범위(이상, 이하)
        if switch_num <= n // 2:
            for i in range(1, switch_num):
                if switches[switch_num - i] == switches[switch_num + i]:
                    left -= 1
                    right += 1
                else:
                    break
        else:
            for i in range(1, n - switch_num + 1):
                if switches[switch_num - i] == switches[switch_num + i]:
                    left -= 1
                    right += 1
                else:
                    break

        # 스위치 누르기
        for j in range(left, right + 1):
            switches[j] = 1 - switches[j]
    # print("switiches: ",  switches)

del switches[0]  # 인덱스 보정용 삭제
# 20개씩 나눠서 출력해야함
for i, e in enumerate(switches):
    if i and not (i % 20):
        print()
    print(e, end=' ')

# 소요 시간 : 19분 53.40초
