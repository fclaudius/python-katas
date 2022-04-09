def high_and_low(numbers):
    lst_nums = []
    for num in numbers.split(" "):
        lst_nums.append(int(num))
    return f"{max(lst_nums)} {min(lst_nums)}"
