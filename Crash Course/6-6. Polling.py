favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'george': 'javascript',
    'amanda': 'java',
    'anthony': 'c',
    'sabrina': 'python',
    'stefanie': 'java'
}

people_to_be_polled = ['sarah', 'phil', 'anthony', 'amanda', 'edward',
                       'carol', 'diana', 'jim', 'natalie', 'steve']

for p in people_to_be_polled:
    if p in favorite_languages:
        print(
            f'Thank you for having taken the poll, {p.title()}.\n'
            f'Your favorite language is {favorite_languages[p].title()}.')
    else:
        print(f'Please take our poll on favorite languages, {p.title()}.')
