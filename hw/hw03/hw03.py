 HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    
    a = n - 1
    b = n - 2
    c = n - 3
    total = 0

    if n <= 3:
        return n
    while n > 3:
        if a <=3:
            #print(a)
            total += a
        if b <=3:
            #print(b)
            total += b * 2
        if c <=3:
            #print(c)
            total += c * 3
        #print(n)
        n = n - 1
        a = n - 1
        b = n - 2
        c = n - 3
    return total




def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k < 7:
        return False
    if k == 7:
        return True
    elif k % 10  == 7:
        return True
    else:
        return has_seven(k // 10)
    return False 



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def direction(position, number, going):
        if has_seven(position) or position % 7 == 0:
            return result(position, number, not going)
        else:
            return result(position, number, going)

    def result(position, number, going): 
        if position == n:
            return number
        elif going:
            return direction(position + 1, number + 1, going)
        else:
            return direction(position + 1, number - 1, going)

    return result(1, 1, True)

 
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    

    def use_coin(amount, coin): 
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif coin > amount:
            return 0
        else:
            return use_coin(amount - coin, coin) + use_coin(amount, coin * 2)

    return use_coin(amount, 1)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    if n == 1:
        return print_move(start, end)
   
    else:
        holder = 6 - start - end
        move_stack(n-1, start, holder) 
        move_stack(1, start, end)
        move_stack(n-1, holder, end)  



def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    
    if lst == []:
        return []
    else:
        if type(lst[0]) == list:
            return flatten(lst[0]) + flatten(lst[1:])
        else:
            return [lst[0]]+ flatten(lst[1:])

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    
    if lst1 == [] and lst2 != []:
        return lst2
    elif lst2 == [] and lst1 != []:
        return lst1
    else:
        if lst1[0] < lst2[0]:
            return [lst1[0]] + merge(lst1[1:], lst2)
        elif lst2[0] < lst1[0]:
            return [lst2[0]] + merge(lst1, lst2[1:])
        elif lst1[0] == lst2[0]:
            return [lst1[0]] + [lst2[0]] + merge(lst1[1:], lst2[1:])

     

    


def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """

    if len(seq) < 2:
        return seq
    
    half = len(seq) // 2
    seq1 = mergesort(seq[:half])
    seq2 = mergesort(seq[half:])
    return merge(seq1, seq2)



    

