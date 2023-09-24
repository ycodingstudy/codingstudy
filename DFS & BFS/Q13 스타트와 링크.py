n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
group_size = n//2
min_val = int(1e9)

def count_group_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                score += graph[team[i]][team[j]]
    return score

def dfs(member, team_start, team_link):
    global min_val
    if len(team_start) == group_size and len(team_link) == group_size: #팀 인원이 전부 찼으면
        score = abs(count_group_score(team_start) - count_group_score(team_link))
        min_val = min(min_val, score)
        return
    if member == n:
        return
    team_start.append(member)
    dfs(member+1, team_start, team_link)
    team_start.pop()
    team_link.append(member)
    dfs(member+1, team_start, team_link)
    team_link.pop()

dfs(0, [], [])
print(min_val)
