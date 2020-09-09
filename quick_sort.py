from cal_time import *
import random
import copy


def _quick_sort(data, left, right):
    if left < right:  # 至少两个元素
        mid = partition(data, left, right)
        _quick_sort(data, left, mid - 1)
        _quick_sort(data, mid + 1, right)
    return data


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:  # 从右边找小于tmp的数，放到左边
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:  # 从左边找大于tmp的数，放到右边
            left += 1
        data[right] = data[left]  # tmp归位
    data[left] = tmp
    return left


@cal_time
def quick_sort(data):
    _quick_sort(data, 0, len(data) - 1)
    return data


li = list(range(100000))
random.shuffle(li)
quick_sort(li)
print(li)
