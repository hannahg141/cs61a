## List Mutation ##
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    for item in range(len(lst)):
        lst[item] = fn(lst[item]) #need to say that its 

    # lst[:] = [fn(item) for item in lst]

def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    # counter = 0
    # for item in range(len(lst)):
    #     if not pred(lst[counter]):
    #         lst.pop(counter)
    #         counter -= 1
    #     counter += 1

    lst[:] = [item for item in lst if pred(item)]

# index (the position item) vs element (the thing, lst[item[]]) in a list
    

## Dictionaries ##

def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for key in d:
        if d[key] == x:
            d[key] = y
    #         return True 
    # return False




















