import sys

h, w = map(int, input().split())

result_sky = []
for i in range(h):
    lst = list(sys.stdin.readline().rstrip())

    for j in range(w):
        if lst[j] == 'c': #구름인 경우 무조건 0으로 초기화
            lst[j] = 0

        elif type(lst[j-1]) == int: # 이전이 구름이 라면
            lst[j] = lst[j - 1] + 1 # 그 전의 값 + 1

    for j in range(w):
        if type(lst[j]) == str: # 구름이 안가면 .이므로 str과 같은지 비교
            lst[j] = -1 # 구름이 안간 곳이기 때문에 -1로 초기화
    result_sky.append(lst) # 결과로 나온 리스트를 append

for i in range(h):
    for j in range(w):
        print(result_sky[i][j], end = ' ')
    print()