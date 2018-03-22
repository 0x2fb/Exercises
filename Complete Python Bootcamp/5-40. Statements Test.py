st = 'Print only the words that start with s in this sentence'
print(f"{', '.join(word for word in st.split() if word[0].lower() == 's')}")
print('_' * 50 + "\n")
print(f"{', '.join(str(x) for x in range(0, 11) if x % 2 == 0)}")
print('_' * 50 + "\n")
print(f"{', '.join(str(x) for x in range(1, 51) if x % 3 == 0)}")
print('_' * 50 + "\n")
st = 'Print every word in this sentence that has an even number of letters'
print(f"{', '.join(word for word in st.split() if len(word) % 2 == 0)}")
print('_' * 50 + "\n")
print(f"{', '.join(word for word in st.split() if len(word) % 2 == 0)}")
fizzbuzz = []
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        fizzbuzz.append('FizzBuzz')
    elif x % 3 == 0:
        fizzbuzz.append('Fizz')
    elif x % 5 == 0:
        fizzbuzz.append('Buzz')
    else:
        fizzbuzz.append(str(x))
print(f"{', '.join(word for word in fizzbuzz)}")
print('_' * 50 + "\n")
st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split()])
