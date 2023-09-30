import sys

n = int(sys.stdin.readline())

score_lst = []
for i in range(n):
    name, language, english, math = sys.stdin.readline().split()
    score_lst.append([name, int(language), int(english), int(math)])

score_lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for idx in range(len(score_lst)):
    print(score_lst[idx][0])
