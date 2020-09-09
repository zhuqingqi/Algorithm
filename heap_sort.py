import random
from cal_time import *

def sift(data, low, high): # sift：筛选     农村包围城市
    """
    :param data: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个节点位置
    :return:
    """
    i = low # i最开始指向根节点
    j = 2 * i + 1  # j 最开始指向左孩子节点
    tmp = data[low]  # 把堆定存起来
    while j <= high:  # 当j不越界的时候
        if j + 1 <= high and data[j] < data[j+1]:  # 若右孩子较大，j指向右孩子节点
            j = j + 1
        if data[j] > tmp:
            data[i] = data[j]
            i = j # 往下走
            j = i * 2 + 1
        else:
            data[i] = tmp
            break
    else:
        data[i] = tmp  # 把tmp放到叶子节点上


@cal_time
def heap_sort(data):
    n = len(data)
    for i in range((n-2)//2, -1, -1):  # 表示建堆的时候调整的根的下标,堆每一给村调整
        sift(data, i, n-1)
    # 此时大根堆已建堆完成,然后挨个出数
    for i in range(n-1, -1, -1):  # i 指向当前的最后一个元素
        data[i], data[0] = data[0], data[i]
        sift(data, 0, i-1)  # i-1 是新的high
    return data

li = list(range(100000))
random.shuffle(li)
print(heap_sort(li))


# import  heapq
# heapq.heapify(li)  # 建一个小根堆
# for i in range(n):
#     print(heapq.heappop(li), end=',') # 每次弹出一个最小元素, 小的先出，类似优先队列