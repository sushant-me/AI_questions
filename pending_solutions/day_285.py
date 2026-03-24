def swap_odd_even_bits(n):
    """ Write a program to swap odd and even bits. """
    # Create masks for extracting odd and even bits
    odd_mask = 0xAAAAAAAA
    even_mask = 0x55555555
    
    # Extract odd and even bits using the masks
    odd_bits = n & odd_mask
    even_bits = n & even_mask
    
    # Shift odd bits right and even bits left to swap them
    odd_bits >>= 1
    even_bits <<= 1
    
    # Combine swapped bits
    result = (odd_bits | even_bits)
    
    return result

# Example usage:
n = 0b1010101010101010
print(bin(swap_odd_even_bits(n)))  # Output: 0b0101010101010101