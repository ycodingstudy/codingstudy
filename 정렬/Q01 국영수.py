n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = map(str,input().split())
    arr.append([name,int(kor),int(eng),int(math)])

sorted_arr = sorted(arr, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for i in sorted_arr:
    print(i[0])