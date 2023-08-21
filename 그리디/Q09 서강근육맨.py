N = int(input())
arr = sorted(list(map(int,input().split())), reverse=True)
temp = 0
if N % 2 != 0:
    temp = arr.pop(0)

minVal = -1
while len(arr) > 0:
    minVal = max(arr.pop(0) + arr.pop(-1), minVal)

print(max(minVal, temp))