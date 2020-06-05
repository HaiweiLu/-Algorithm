def shellSort(alist):
    # 设定间隔
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        # 子列表排序
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)

        # 间隔减小
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap        

        alist[position] = currentvalue

# test
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)