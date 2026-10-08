"""
DSA Python Wala — Day 3
Topic: Counting Non-Zero Digits

This program counts how many non-zero digits
are present in an integer.

First, n stores the integer 7005.
The while loop continues as long as n is greater than 0.

The modulo operator (%) with 10 extracts the last digit
and stores it in r.

If r is not equal to 0, count is increased by 1.

Then //= 10 removes the last digit from n.

For 7005:

7005 % 10 → 5 → count = 1
700  % 10 → 0 → no change
70   % 10 → 0 → no change
7    % 10 → 7 → count = 2

Therefore, the output is: 2
"""

n = 7005
count = 0

while n > 0:
    r = n % 10
    if r != 0:
        count += 1
    n //= 10

print(count)