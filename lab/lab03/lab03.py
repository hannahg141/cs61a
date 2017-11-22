"""Lab 3: Recursion and Tree Recursion"""

# Q1
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if a == 0:
        return c
    else:
        return b + ab_plus_c(a-1, b, c) #i want b to be added a times, so if b = 5 and a = 2, i want to add b 2 times (5 + 5 = 10) and once a is 0, add c

# Q2
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    #GREATEST not lowest **, the largest number that that can divide BOTH numbers
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b 
    return gcd(a % b, b)

    


# Q3
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    if n == 1:
        print(n)
        return 1 
    elif n % 2 == 0:
        print(n)
        return 1 + hailstone(n // 2)
    else:
        print(n)
        return 1 + hailstone((n * 3) + 1)










