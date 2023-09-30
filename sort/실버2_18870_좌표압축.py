n = int(input())
graph = list(map(int, input().split()))
dic = dict()

sort_graph = sorted(graph)
sort_graph = sorted(list(set(sort_graph)))

for i in range(len(sort_graph)):
    dic[sort_graph[i]] = i

for num in graph:
    print(dic[num], end = ' ')