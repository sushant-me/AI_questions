"""
Implement deque using collections.
"""

from collections import deque

# Example usage:
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # Output: deque([0, 1, 2, 3, 4])
dq.pop()
dq.popleft()
print(dq)  # Output: deque([1, 2, 3])