# 문제 풀이 아이디어
# 맨처음 sort() 한다음 작은것 부터 두개를 고른다
# 그리고 더 큰 쪽에 담은 뒤에 다시 리스트에 넣고 가장 작은 것과 그다음 작은것을 고른다


import sys

n = int(sys.stdin.readline())

energy_drink_lst = list(map(int, sys.stdin.readline().split()))
energy_drink_lst.sort()



result = 0
for i in range(len(energy_drink_lst) - 1):
    result += energy_drink_lst[i] / 2

result = energy_drink_lst[-1] + result
print(result)



    # print(energy_drink_lst)
    #
    # smallest_num = energy_drink_lst.pop(0)
    # num = energy_drink_lst.pop(0)
    #
    # smallest_num = smallest_num / 2
    # num += smallest_num
    #
    # energy_drink_lst.insert(0, num)
    #
    # if len(energy_drink_lst) == 1 :
    #     break
    #
    # k = 0
    # while True:
    #     try:
    #
    #         if energy_drink_lst[k] < energy_drink_lst[k + 1]:
    #             break
    #
    #         else:
    #             tmp = energy_drink_lst[k]
    #             energy_drink_lst[k] = energy_drink_lst[k + 1]
    #             energy_drink_lst[k + 1] = tmp
    #
    #         k += 1
    #     except:
    #         break

