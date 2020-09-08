def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j]<li[min_loc]:
                li[j],li[min_loc] = li[min_loc], li[j]
    return li
li = [2,1,4,6,8,3,3,0,5,7,9]
print(select_sort(li))