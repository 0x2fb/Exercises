def find_greater_numbers(ls):
    if ls == []:
        return 0
    count = 0
    for i in range(0, len(ls) - 1):
        for j in range(i, len(ls)):
            if ls[i] < ls[j]:
                count += 1
    return count


print(find_greater_numbers([1, 2, 3]))  # 3
print(find_greater_numbers([6, 1, 2, 7]))  # 4
print(find_greater_numbers([5, 4, 3, 2, 1]))  # 0
print(find_greater_numbers([]))  # 0
