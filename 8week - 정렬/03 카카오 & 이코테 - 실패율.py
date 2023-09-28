# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 실패율 : 스테이지 도달 && 아직 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# N : 전체 스테이지 수 / stages : 게임을 이용한 사용자가 멈춰있는 스테이지 번호
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호를 return
# N+1은 N까지 클리어한 사용자를 의미함
# 스테이지에 도달한 유저가 없는 경우 해당 스태이지의 실패율은 0임

def solution(N, stages):
    cur_dic = {i: 0 for i in range(1, N + 2)}  # 현재 그 스테이지에 있는 사람 수
    total_dic = {i: 0 for i in range(1, N + 2)}  # 그 스테이지를 통과한 사람 수
    for stage in stages:
        cur_dic[stage] += 1
        # 시간초과
        # for i in range(1, stage + 1):
        #     if i != N + 1:
        #         total_dic[i] += 1
    total_dic[N + 1] = cur_dic[N + 1]
    for i in range(N, 0, -1):
        total_dic[i] = total_dic[i + 1] + cur_dic[i]

    res = []  # [(스테이지번호, 실패율), ()]
    for i in range(1, N + 1):
        fail_rate = cur_dic[i] / total_dic[i] if total_dic[i] != 0 else 0
        res.append((i, fail_rate))
    res.sort(key=lambda x: (-x[1], x[0]))
    answer = [item[0] for item in res]
    return answer


n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))

n = 4
stages = [4, 4, 4, 4, 4]
print(solution(n, stages))
