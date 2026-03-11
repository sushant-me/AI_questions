def bubble_sort(lst):
    """
    Write a program to sort a list without using sort().
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example usage:
sorted_list = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(sorted_list)