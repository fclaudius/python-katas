def longest(a1, a2):
    unique_string = dict()
    for element in a1 + a2:
        unique_string[element] = None
    unique_string = sorted(unique_string)
    neu = str()
    for element in unique_string:
        neu += element
    print(neu)
    return neu


longest("aretheyhere","yestheyarehere")
# "aehrsty"
