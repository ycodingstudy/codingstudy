n = int(input())
students = []
# 이름, 국(내림차순), 영(오름차순), 수(내림차순) -> 이후에 이름 사전순
for _ in range(n):
    name, ko, en, math = input().split()
    students.append([name, int(ko), int(en), int(math)])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
