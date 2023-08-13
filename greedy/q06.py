food_times = list(map(int, input().split()))

k = int(input())

result = 0


for i in range(len(food_times)):
    if food_times[i] != 0 :
        food_times[i] = food_times[i] - 1

