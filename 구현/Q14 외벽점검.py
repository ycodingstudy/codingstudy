from itertools import permutations

def solution(n, weak, dist):
    length = len(weak) # 2배로 늘려서 원형을 일자로 변형
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입 할 친구의 최솟값을 찾아야함으로 가장 큰 값
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는  모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약점 확인
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
                if index == start + length - 1: # 모든 취약 지점을 점검 가능한 경우
                    answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer