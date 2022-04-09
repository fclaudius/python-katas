def array_diff(a, b):

    if len(a or b) == 0:
        return a
    for element in b:
        while element in a:
            a.remove(element)
    
    return a
