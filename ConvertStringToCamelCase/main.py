import re


def to_camel_case(text):
    reg1 = re.compile("(_|-)[a-zA-Z]")
    reg2 = re.compile("[a-zA-Z]")
    while re.search(r"_|-", text) is not None:
        text = text.replace( myfirst(text, reg1),  replacement(myfirst(text, reg1), reg2))

    return text


def myfirst(text, reg1):
    my = re.search(reg1, text)
    if my is None:
        my = ""
    else:
        my = str(my.group())
    return my


def replacement(atext, reg2):
    my = re.search(reg2, atext)
    if my is None:
        my = ""
    else:
        my = str(my.group()).upper()
    return my


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))