import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
INF = 2147000000

graph = []
house_coordinate = []
chicken_coordinate = []
for i in range(n):
    tmp_graph = list(map(int, sys.stdin.readline().split()))

    for j in tmp_graph :
        if j == 1 :
            house_coordinate.append([i + 1, j + 1])
        elif j == 2 :
            chicken_coordinate.append([i + 1, j + 1])

print(house_coordinate)
print(chicken_coordinate)

# chicken_nCr = list(itertools.combinations(chicken_coordinate, m))
# res = INF
# for i in chicken_nCr:
#     distance_final = 0
#     for house in house_coordinate:
#         distance = INF
#         for j in i:
#             distance = min(distance, abs(j[0] - house[0]) + abs(j[1] - house[1]))
#         distance_final += distance
#     res = min(INF, distance_final)
# print(res)

res = INF
for x in itertools.combinations(chicken_coordinate, m):
    city_dist = 0
    for h in house_coordinate:
        house_dist = INF
        for k in x:
            house_dist = min(house_dist, abs(h[0] - k[0]) + abs(h[1] - k[1]))
        city_dist += house_dist
    res = min(res, city_dist)

print(res)



        #distance_group.append(min(distance))
    #distance_final_group.append(sum(distance_group))
#
# print(distance_final_group)
    # for j in i:
    #     distance = 0
    #     for house in house_coordinate:
    #         distance = abs(j[0] - house[0]) + abs(j[1] - house[1])
    #         print(j)
    #     print(123123123123)
    #     distance_group.append(distance)

# print(distance_group)


