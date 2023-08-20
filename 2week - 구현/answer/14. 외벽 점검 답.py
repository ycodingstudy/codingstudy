from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)  # 같은 weak를 두번 표시하기 위함

    answer = len(dist) + 1  # answer : 투입할 친구의 수의 최솟값 (우선 친구 수 보다 많게 작성)

    for start in range(length):  # 기존 weak의 길이 만큼(처음 들어가는 지점 위치)
        for friends in list(permutations(dist, len(dist))):
            cnt = 1  # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[cnt - 1]  # 문제 지점부터 시작해서 자기가 갈 최대
            # 시작 점(weak별 1개씩)부터 모든 취약 지점 확인
            for index in range(start, start + length):  # 처음 들어가는 곳에서 weak지점의 전체 길이만큼 하나씩 확인
                if position < weak[index]:  # 갈 수 있는 최대 < 특정 weak 지점
                    cnt += 1  # 새친구 투입
                    if cnt > len(dist):  # 더이상 투입이 불가능 하면 종료
                        break
                    position = weak[index] + friends[cnt - 1]  # 새로 투입된 친구가 갈 수 있는 최대 거리
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer
