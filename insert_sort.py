import time
from cal_time import *
import random

@cal_time
def insert_sort(data):
    for i in range(1, len(data)): #i 表示摸到牌的下标
        tmp = data[i]
        j = i - 1 # j 表示抽出的牌的下标
        while j>=0 and data[j]>tmp:
            data[j + 1] = data[j]
            j = j-1
        data[j + 1] = tmp
    return data


# lis = [2,1,4,6,8,3,0,5,7,9]
# insert_sort(lis)


li = list(range(1000))
random.shuffle(li)
# li1 = copy.deepcopy(li)
insert_sort(li)