#메모리 초과
def hanoi(n, start, temp, end, moved):
    if n == 1:
        moved.append([start, end])
        return
    hanoi(n-1, start, end, temp, moved) #temp에 n-1만큼 전부 이동
    moved.append([start, end]) #n번째를 마지막으로 이동시킨다.
    hanoi(n-1, temp, start, end, moved) #temp에 있는 원판을 end로 전부 이동

n = int(input())
moved = []
hanoi(n, 1, 2, 3, moved)
print(len(moved))

if n <= 20:
    for m in moved:
        print(*m)