def max_difference(numbers):
    if not numbers:
        return None
    min_num = max_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return max_num - min_num