"""
1–10: Basic Python
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def sum_of_list(lst):
    return sum(lst)

def remove_duplicates(lst):
    return list(set(lst))

def count_elements(lst):
    return {x: lst.count(x) for x in lst}

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def calculate_area(length, width):
    return length * width

def calculate_volume(length, width, height):
    return length * width * height

def format_currency(amount):
    return f"${amount:,.2f}"

def main():
    print(fibonacci(10))  # Output: 55
    print(is_prime(29))  # Output: True
    print(reverse_string("Python"))  # Output: nohtyP
    print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
    print(count_elements([1, 2, 2, 3, 4, 4, 5]))  # Output: {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
    print(find_max([1, 2, 3, 4, 5]))  # Output: 5
    print(find_min([1, 2, 3, 4, 5]))  # Output: 1
    print(calculate_area(5, 3))  # Output: 15
    print(calculate_volume(5, 3, 2))  # Output: 30
    print(format_currency(1234.5678))  # Output: $1,234.57

if __name__ == "__main__":
    main()