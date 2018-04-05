def same_frequency(n1, n2):
    s1 = set([int(i) for i in str(n1)])
    s2 = set([int(i) for i in str(n2)])
    return [str(n1).count(str(i)) for i in s1] == [str(n2).count(str(i)) for i in s2]


print(same_frequency(551122, 221515))  # True
print(same_frequency(321142, 3212215))  # False
print(same_frequency(1212, 2211))  # True
