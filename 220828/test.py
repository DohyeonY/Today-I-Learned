n = int(input())
num_list = list(map(int, input().split()))

result = 1
increase_temp = 1
decrease_temp = 1

for i in range(0, n - 1):
    if num_list[i] <= num_list[i + 1]:
        increase_temp += 1
        if increase_temp > result:
            result = increase_temp

    else:
        increase_temp = 1

for j in range(0, n - 1):
    if num_list[j] >= num_list[j + 1]:
        decrease_temp += 1
        if decrease_temp > result:
            result = decrease_temp
    else:
        decrease_temp = 1

print(result)