import sys

n = int(sys.stdin.readline())
horror_lst = sorted(list(map(int, sys.stdin.readline().split())))

horror_lst.sort()

# print(horror_lst)

group_cnt = 0
group_tmp_lst = []
for i in range(len(horror_lst)):
    group_tmp_lst.append(horror_lst[i])
    if group_tmp_lst[i] == len(group_tmp_lst):
        group_cnt += 1

print(group_cnt)
