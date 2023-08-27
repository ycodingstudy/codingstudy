n = int(input())
lst = list(map(int, input().split()))
lst.sort() # 정렬



result_lst = []
result = 0
if n % 2 == 0 :     # n이 짝수인 경우
    for i in range(n // 2):
        result = lst[i] + lst[n - i - 1]
        result_lst.append(result)

elif n % 2 == 1 :   # n이 홀수인 경우
    tmp = lst.pop()
    for i in range(n // 2):
        result = lst[i] + lst[n - i -2]
        result_lst.append(result)
    result_lst.append(tmp)

print(max(result_lst))
