def my_for(my_iterable, my_range, my_function):
    iterator = iter(my_iterable)
    count = int(my_range)
    while count > 0:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            my_function(i)
            count -= 1


my_for([1, 2, 3, 4, 5, 6], 4, print)
