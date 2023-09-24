# 삽입정렬 : 데이터를 필요할 때만 위치를 바꿈
# -> 어느정도 정렬이 되어 있을 때 매우 유리
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
