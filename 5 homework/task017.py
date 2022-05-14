import re


def abbreviation(st):
    pattern = r'\b[А-ЯA-Z]{2,}(?: ?[А-ЯA-Z]{2,})*\b'
    return re.findall(pattern, st)
