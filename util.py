from bisect import bisect_left
from config import Artist, Album


def binary_search(array, s):
    i = bisect_left(array, s)
    if i != len(array) and array[i].name == s.name:
        return i
    return -1
