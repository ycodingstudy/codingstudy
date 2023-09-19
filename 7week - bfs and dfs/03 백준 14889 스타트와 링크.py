from itertools import combinations

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def cal_ability(s_team, l_team):
    s_sum, l_sum = 0, 0
    for i, j in combinations(s_team, 2):
        s_sum += board[i-1][j-1] + board[j-1][i-1]
    for i, j in combinations(l_team, 2):
        l_sum += board[i-1][j-1] + board[j-1][i-1]
    return abs(s_sum - l_sum)


# n//2명의 팀을 나누는 방법
s_team = []
l_team = []

visited = [False] * n
min_diff = int(1e9)
def dfs(depth, n, people_idx): # depth : 깊이, n, 전체 인원, people_idx : 사람을 다양한 위치에서 탐색하기 위함
    global min_diff

    if depth == n // 2:
        # 절반으로 나누면서
        # visited 처리되지 않은 사람들을 l team으로 넣음
        for i in range(n):
            if not visited[i]:
                l_team.append(i+1)
        min_diff = min(min_diff, cal_ability(s_team, l_team))
        l_team.clear() # 한 바퀴 돌고 l_team을 비워줌 (새로 업뎃 필요)
        return

    for i in range(people_idx, n):
        if not visited[i]:
            visited[i] = True
            s_team.append(i+1)

            dfs(depth+1, n, i+1)

            s_team.pop() # 백트래킹
            visited[i] = False

dfs(0,n,0)
print(min_diff)