"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    while n > 0:
        x = f(x)
        n -= 1
    return x





def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    sum = 0
    while n > 0:
        sum += n % 10 
        n = n // 10
    return sum 



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    total = len(str(n))
    while total > 0:
        if n % 10 == 8 and (n // 10) % 10 == 8:
            n = n // 10
            total -= 1
            return True
        else:
            total -= 1
            n = n // 10
    return False
            


           


#if n % 10 == 8:
 #           return True
  #          total -= 1
   #     if n % 10 == 8:
    #        n = n // 10
     #   if n % 10 == 8:
      #      return True








