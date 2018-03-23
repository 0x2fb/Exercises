x = ((((3*10)-10) ** 2)+1)/4
print(x)
print('_' * 50 + "\n")
print(2/3)
print(44, 29, 34)
print('_' * 50 + "\n")
print("float")
print('_' * 50 + "\n")
print("x ** 2 ... x ** 0,5")
print('_' * 50 + "\n")
s = 'hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])
print('_' * 50 + "\n")
print([0, 0, 0])
print([0 for _ in range(3)])
l = [1, 2, [3, 4, 'hello']]
l[2][2] = 'goodbye'
print(l)
l = [5, 3, 4, 6, 1]
l.sort()
print(l)
print('_' * 50 + "\n")
d = {'simple_key': 'hello'}
print(d['simple_key'])
d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
print('_' * 50 + "\n")
l = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(list(set(l)))
print(2 > 3)  # False
print(3 <= 2)  # False
print(3 == 2.0)  # False
print(3.0 == 3)  # True
print(4**0.5 != 2)  # False
print('_' * 50 + "\n")
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
print(l_one[2][0] >= l_two[2]['k1'])  # False
