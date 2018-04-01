import re


def censor(s):
    pattern = re.compile(r'\b\w*frack\w*\b', re.I)
    return pattern.sub('CENSORED', s)
