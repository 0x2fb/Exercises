def letter_counter(my_string):
    def inner(letter):
        return my_string.lower().count(letter)
    return inner


counter = letter_counter('Amazing')
print(counter('a'))  # 2
print(counter('m'))  # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))  # 2
print(counter2('t'))  # 1
