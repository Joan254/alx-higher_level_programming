#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list of integers): List of integers to find the peak of
    Returns: 
        int or None: Peak of list_of_integers or None if the list is empty
    """
    arr_size = len(list_of_integers)
    mid_estimate = arr_size
    mid = arr_size // 2

    if arr_size == 0:
        return None

    while True:
        mid_estimate = mid_estimate // 2
        if (mid < arr_size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_estimate // 2 == 0:
                mid_estimate = 2
            mid = mid + mid_estimate // 2
        elif mid_estimate > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_estimate // 2 == 0:
                mid_estimate = 2
            mid = mid - mid_estimate // 2
        else:
            return list_of_integers[mid] 
