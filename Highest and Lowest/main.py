def high_and_low(numbers):
    lst_nums = []
    for num in numbers.split(" "):
        lst_nums.append(int(num))

    lst_nums.sort()
    min_num = lst_nums[0]
    max_num = lst_nums[len(lst_nums)-1]
    return f"{max_num} {min_num}"

