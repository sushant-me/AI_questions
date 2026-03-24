def generate_gray_codes(n):
    if n == 0:
        return ['0']
    if n == 1:
        return ['0', '1']

    previous = generate_gray_codes(n - 1)
    prefix_0 = ['0' + code for code in previous]
    prefix_1 = ['1' + code for code in reversed(previous)]
    return prefix_0 + prefix_1

# Example usage
n = 3
gray_codes = generate_gray_codes(n)
print(gray_codes)