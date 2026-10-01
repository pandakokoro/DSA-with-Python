"""
This program extracts and prints the digits of an integer from right to left.

First, n stores the integer 5183.
The while loop continues as long as n is greater than 0.
The modulo operator (%) with 10 extracts the last digit of n
and stores it in r.
The extracted digit is printed with a space.
Then //= 10 removes the last digit from n.
This process continues until n becomes 0.

For 5183:
5183 % 10 → 3
518  % 10 → 8
51   % 10 → 1
5    % 10 → 5

Therefore, the output is: 3 8 1 5
"""

n = 5183

while n > 0:
    r = n % 10
    print(r, end=" ")
    n //= 10