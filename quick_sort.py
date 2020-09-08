def quick_sort(li, left, right):
    if left < right: #至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)
    return li


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:#从右边找小于tmp的数，放到左边
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:#从左边找大于tmp的数，放到右边
            left += 1
        li[right] = li[left] #tmp归位
    li[left] = tmp
    return left

li = [2,1,4,6,8,3,3,0,5,7,9]
print(quick_sort(li, 0, len(li)-1))