from lab05 import *

## Extra Questions ##

## Linked Lists ##

def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    if s0 == empty:
        return s1
    if s1 == empty: # or rest(s0) == empty or rest(s1) == empty:
        return s0
    else:
        return link(first(s0), link(first(s1), interleave(rest(s0), rest(s0))))
    # if first(s0) < first(s1):
    #     return link(first(s0), interleave(rest(s0), s1))
    # else:
    #     return link(first(s1), interleave(s0, rest(s1)))

def filter_list(predicate, lst):
    """Returns a link only containing elements in lst that satisfy
    predicate.

    >>> lst = link(25, link(5, link(50, link(49, link(80, empty)))))
    >>> new = filter_list(lambda x : x % 2 == 0, lst)
    >>> print_link(new)
    50 80
    """
    if lst == empty:
        return empty 
    
    if predicate(first(lst)):
        return link(first(lst), filter_list(predicate, rest(lst)))
    else:
        return filter_list(predicate, rest((lst)))
   
## Trees ##

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    if root(t) == category:
        return tree(root(t), branches(t)+[tree(song)])
    
    return tree(root(t), [add_song(b, song, category) for b in branches(t)])
            
def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    keeping = []
    for b in branches(t):
        if root(b) != target:
            keeping += [delete(b, target)]
    return tree(root(t), keeping)


    #make a list of the branches we WANT to KEEP, only add if the root isnt equal to the target, and then make a new treee
