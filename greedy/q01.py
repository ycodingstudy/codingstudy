import sys

n = int(sys.stdin.readline())

horror_lst = list(map(int, sys.stdin.readline().split()))
# 2 3 1 2 2

horror_lst.sort()
# 1 2 2 2 3



group_cnt = 0
group_tmp_lst = []
for i in range(len(horror_lst)): # 5
    group_tmp_lst.append(horror_lst[i]) # 1

    if group_tmp_lst[-1] == len(group_tmp_lst):
        group_cnt += 1
        group_tmp_lst = []

print(group_cnt)
