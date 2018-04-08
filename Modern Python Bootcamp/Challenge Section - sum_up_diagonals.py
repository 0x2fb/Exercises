def sum_up_diagonals(*args):
    # sum1 = 0
    # sum2 = 0
    # for i, ls in enumerate(args[0]):
    #     sum1 += ls[i]
    #     sum2 += ls[len(args[0]) - i - 1]
    # return sum1 + sum2
    return sum((ls[i] + ls[len(args[0]) - i - 1] for i, ls in enumerate(args[0])))


list1 = [[1, 2], [3, 4]]
print(sum_up_diagonals(list1))  # 10
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_up_diagonals(list2))  # 30
list3 = [[4, 1, 0], [-1, -1, 0], [0, 0, 9]]
print(sum_up_diagonals(list3))  # 11
list4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(sum_up_diagonals(list4))  # 68
