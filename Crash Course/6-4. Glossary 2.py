glossary = {
    'class': 'template for objects',
    'global': 'global scope for variables',
    'nonlocal': 'variables in higher scope , '
    'e.g. main functions but not local',
    'raw string': 'easy string formatting for regular expressions',
    'kwargs': 'keyword-value pairings for function paramters',
    'lambda': 'anonymous function',
    'map object': 'uses a function (often lambda) on an iterable',
    'filter object': 'uses a function (often lambda) on an iterable '
    'and only returns True values',
    'subclass': 'class that is part of a parent class',
    'set': 'an iterable object with no indices and no duplicates'
}

for k, v in glossary.items():
    print(f'{k}: {v}\n')
