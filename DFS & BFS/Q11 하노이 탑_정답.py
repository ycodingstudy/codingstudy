def hanoi(n, start, temp, end):
    if n == 1:
        print(start, end, sep=" ")
        return
    hanoi(n-1, start, end, temp) #temp에 n-1만큼 전부 이동
    hanoi(1, start, temp, end) #현재 원판을 마지막으로 이동
    hanoi(n-1, temp, start, end) #temp에 있는 원판을 end로 전부 이동

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 2, 3)