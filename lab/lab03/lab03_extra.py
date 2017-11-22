from lab03 import *

# Q4
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

# Q5
def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        while i <= n:
            print(i)
            i += 1
    counter(1)

# Q6

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i +=1  
    return True

# Q7
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    total, i = 0, 1
    while i <= n:
        total += odd_term(i)
        i += 1
        total += even_term(i)
        i += 1
    return total
    #1 + 4 + 3 + 16 + 5 



# Q8
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + helper(n // 10, 10 - n % 10)



def helper(n, digit):
    if n == 0:
        return 0
    else:
        if n % 10 == digit:
            return 1 + helper(n // 10, digit)
        else:
            return helper(n // 10, digit)
    
        



