def three_odd_numbers(ls):
    # for i in range(0, len(ls) - 2):
    #     if sum((ls[i], ls[i + 1], ls[i + 2])) % 2 != 0:
    #         return True
    # return False
    return any(
        sum((ls[i], ls[i + 1], ls[i + 2])
            ) % 2 != 0 for i in range(0, len(ls) - 2))


print(three_odd_numbers([1, 2, 3, 4, 5]))  # True
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))  # True
print(three_odd_numbers([5, 2, 1]))  # False
print(three_odd_numbers([1, 2, 3, 3, 2]))  # False
