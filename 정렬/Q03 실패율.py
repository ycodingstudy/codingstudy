def solution(N, stages):
    answer = []
    cnt = len(stages)
    temp = []
    for i in range(N):
        if stages.count(i+1) > 0:
            temp.append([stages.count(i+1) / cnt, i+1])
        else:
            temp.append([0,i+1])
        cnt -= stages.count(i+1)
        print(str(stages.count(i+1)) + " cnt = "+str(cnt))
    print(sorted(temp, key=lambda x:(-x[0])))
    for i in sorted(temp, key=lambda x:(-x[0])):
        answer.append(i[1])
    return answer