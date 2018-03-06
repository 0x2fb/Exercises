pets = [
    {"cat": "Jack"},
    {"dog": "Mike"},
    {"guinea pig": "Martha"},
    {"rabbit": "Frank"},
    {"hamster": "Luther"}
]

for i in pets:
    for k, v in i.items():
        print(f'{v}\'s pet is a {k}.')
