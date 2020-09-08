from cal_time import *
import time


@cal_time
def linear_search(lis, val):
    for ind, v in enumerate(lis):
        if v == val:
            return ind
        else:
            return None


@cal_time
def binary_search(lis, val):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == val:
            return mid
        elif lis[mid] > val:
            right = mid - 1
        elif lis[mid] < val:
            left = mid + 1
    else:
        return None


li = list(range(1000))
print(binary_search(li, 354))
print(linear_search(li, 354))
