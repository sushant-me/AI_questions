"""
Profile Python program.
"""

import cProfile

def profile_program():
    # Example function to profile
    def example_function():
        total = 0
        for i in range(1000000):
            total += i
        return total

    cProfile.run('example_function()')

if __name__ == "__main__":
    profile_program()