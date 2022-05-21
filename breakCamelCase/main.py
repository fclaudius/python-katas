import re


def solution(s):
    s = str(s)
    found = set(re.findall(r"[^ ]([A-Z])", s))
    for item in found:
        s = s.replace(item, f' {item}')
    return s
