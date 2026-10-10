
"""
DSA Python Wala — Day 4
Topic: Conditional Digit Counting

This program counts digits that satisfy at least one condition:
1. The digit is smaller than 5.
2. The digit is odd.

The modulo operator (%) extracts the last digit.
The OR operator allows a digit to qualify if either
condition is true.
The //= operator removes the last digit.

For n = 583624:
Digits smaller than 5: 3, 2, 4
Odd digits: 3, 5

The qualifying digits are 3, 2, 4, 5.
Therefore, the output is 4.
"""

n = 583624
count = 0

while n > 0:
    r = n % 10

    if r < 5 or r % 2 != 0:
        count += 1

    n //= 10

print(count)
