def bubble_sort_1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return

    return None


lis = [2,1,4,6,8,3,0,5,7,9]
print(lis)
bubble_sort_1(lis)