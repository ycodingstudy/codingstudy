def solution(N, stages):
    result = []
    answer = []
    people = len(stages)
    for i in range(1, N + 1):
        stage_cnt = stages.count(i)

        if people == 0:
            failure_rate = 0
        else:
            failure_rate = stage_cnt / people

        result.append([i, failure_rate])
        people -= stage_cnt

    result.sort(key=lambda x: [-x[1], x[0]])
    for j in range(N):
        answer.append(result[j][0])
    return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))