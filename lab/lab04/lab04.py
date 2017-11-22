# Q2
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for element in i_list:
        if element > this:
            print(element)
        else:
            print('that')

# Q4
#function, sequence, lower bound, upper bound
    #returns a list of coordinate pairs [x, fn(x)] (x, y)
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[i, fn(i)] for i in seq if (fn(i) >= lower and fn(i) <= upper)]

# Q5
def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    

    return sqrt(((get_lat(city1) - get_lat(city2)) ** 2) + (get_lon(city1) - get_lon(city2)) ** 2)
# Q6
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """

    distance1 = sqrt(((get_lat(city1) - lat) ** 2) + (get_lon(city1) - lon) ** 2)
    distance2 = sqrt(((lat - get_lat(city2)) ** 2) + (lon - get_lon(city2)) ** 2)

    if distance1 > distance2:
        return get_name(city2)
    else:
        return get_name(city1)

    # city1 = make_city(city1, lat, lon)
    # city2 = make_city(city2, lat, lon)
    # city1_distance = distance(city1, (lat, lon))
    # city2_distance = distance(city2, (lat, lon))
    # if city1_distance > city2_distance:
    #     return city1
    # else:
    #     return city2


















