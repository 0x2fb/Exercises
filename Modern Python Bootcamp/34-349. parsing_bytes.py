import re


def parse_bytes(s):
    pattern = re.compile(r'\b[0,1]{8}\b')
    return pattern.findall(s)
