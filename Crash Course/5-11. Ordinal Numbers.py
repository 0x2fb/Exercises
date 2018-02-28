ordinal_numbers = [str(i) + ('st' if str(i)[-1] == '1' else 'nd' if str(i)[-1] ==
                             '2' else 'rd' if str(i)[-1] == '3' else 'th')
                   for i in range(1, 50)]
print(ordinal_numbers)
