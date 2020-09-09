from cal_time import *
import random


@cal_time
def bubble_sort_1(data):
    for i in range(len(data) - 1):
        exchange = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                exchange = True
        #print(data)
        if not exchange:
            return

    return None


# lis = [2,1,4,6,8,3,0,5,7,9]
# print(lis)
# bubble_sort_1(lis)

li = list(range(100))
random.shuffle(li)
# li1 = copy.deepcopy(li)
bubble_sort_1(li)
print(li)