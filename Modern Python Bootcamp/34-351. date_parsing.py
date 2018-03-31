import re


def parse_date(s):
    pattern = re.compile(
        r'\b(?P<d>[0-3]\d)[./,](?P<m>[0,1]\d)[./,](?P<y>\d{4})\b')
    match = pattern.search(s)
    if match:
        d, m, y = match.group('d', 'm', 'y')
        return {'d': d, 'm': m, 'y': y}


print(parse_date('21.03.1234'))
