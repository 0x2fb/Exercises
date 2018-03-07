person = {
    'Helen': [3, 5, 22, 78, 16],
    'Steve': [7, 34, 56, 78, 98],
    'Amanda': [1, 2, 3, 99, 94],
    'Laura': [33, 44, 55, 66, 77]
}

for k, v in person.items():
    print(
        f"{k}'s favorite numbers are "
        f"{', '.join(map(lambda x: str(x), v[0:-1]))} and {v[-1]}.")
