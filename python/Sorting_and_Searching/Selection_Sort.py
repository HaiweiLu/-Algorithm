def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0               # 记录一轮比较中最大数的位置
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


# 测试
alist = [12, 2, 5, 23, 31, 7, 9, 10]
selectionSort(alist)
print(alist)
