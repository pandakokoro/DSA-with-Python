
"""
DSA Python Wala — Day 2
Topic: Sum of Digits

1. Store an integer in n.
2. Extract its last digit using % 10.
3. Add that digit to total.
4. Remove the last digit using //= 10.
5. Repeat until n becomes 0.
"""

n = 9368145
total = 0

while n > 0:
    r = n % 10
    total += r
    n //= 10

print(total)