import random


def sift(data, low, high):  # 建立小根堆，即小的数放到堆顶，出数的时候从堆底出，则从大到小排序
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
        if j + 1 <= high and data[j] > data[j+1]:  # 若右孩子较小，j指向右孩子节点
            j = j + 1
        if data[j] < tmp:  # 若子节点比父节点小,则交换父子节点的值
            data[i] = data[j]
            i = j  # 往下走
            j = i * 2 + 1
        else:
            break
        data[i] = tmp


def topk(data, k):
    heap = data[0:k]
    for i in range((k-2)//2, -1, -1):  # 1.用data的前k个数建立小根堆，暂称为k堆
        sift(heap, i, k-1)
    for i in range(k, len(data)-1):
        if heap[0] < data[i]:  # 2.若data的第i个大于k堆底元素,则把第i个元素放到k堆底
            heap[0] = data[i]  #
            sift(heap, 0, k-1)  # 3.重建k堆为小根堆
    for i in range(k-1, -1, -1):  # 只出前k个数
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap


li = list(range(100000))
random.shuffle(li)
print(topk(li, 100))

