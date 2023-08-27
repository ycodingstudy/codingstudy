# # 답지 봤음
# equation_string = input()
#
# #lst = equation_string.split('-')
# result = 0
# tmp = ''
#
# plus_tmp = 0
# flag = 0
# for s in equation_string:
#     if s != '+' and s != '-':
#         tmp += s
#
#     elif s == '+':
#         if flag == 1:
#             plus_tmp += int(tmp)
#         else:
#             result += int(tmp)
#             tmp = ''
#
#     elif s == '-':
#         if flag == 1 :
#             result += -(plus_tmp)
#             tmp = ''
#             plus_tmp = 0
#             flag = 1
#         else: #앞에 -가 없었을때
#             result += int(tmp)
#             tmp = ''
#             flag = 1
#
# if flag == 1 and plus_tmp != 0:
#     result += -(plus_tmp)
#
#
# print(result)


arr = input().split('-')
s = 0
print(arr)
for i in arr[0].split('+'):
    s += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)
