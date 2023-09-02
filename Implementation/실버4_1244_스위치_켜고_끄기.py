number_of_swich = int(input())
swich_lst = list(map(int, input().split()))
number_of_student = int(input())

student_lst = []
for i in range(number_of_student):
    student_lst.append(list(map(int, input().split())))

for student in student_lst:
    if student[0] == 1: # 남학생 일때
        target = student[1] - 1 # 자신이 받은 번호
        while True:
            if target > number_of_swich - 1:
                break
            swich_lst[target] = swich_lst[target] ^ 1

            target += student[1]

    elif student[0] == 2: # 여학생 일때
        target = student[1] - 1 # 자신이 받은 번호

        target_left = target - 1 # 왼쪽
        target_right = target + 1 # 오른쪽

        while True:
            if target_left < 0 or target_right >= number_of_swich:
                target_left += 1
                target_right -= 1
                break

            elif swich_lst[target_left] == swich_lst[target_right]:
                target_left -= 1
                target_right += 1

            else:
                target_left += 1
                target_right -= 1
                break


        for i in range(target_left, target_right + 1):
            swich_lst[i] = swich_lst[i] ^ 1


i = 0
while True:
    if i == number_of_swich:
        break
    print(swich_lst[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
    i+= 1