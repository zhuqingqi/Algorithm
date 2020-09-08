
import time
from cal_time import *

@cal_time
def insert_sort(li):
    for i in range(1, len(li)): #i 表示摸到牌的下标
        tmp = li[i]
        j = i - 1 # j 表示抽出的牌的下标
        while j>=0 and li[j]>tmp:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = tmp
    return li


lis = [2,1,4,6,8,3,0,5,7,9]

print(insert_sort(lis))
