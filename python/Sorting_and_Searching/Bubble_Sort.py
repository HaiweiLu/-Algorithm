def bubbleSort(alist):
    # for i in range(number, 0, -1) 是倒序遍历，即从 number 到 1，go backwards
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                '''
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                '''
                alist[i], alist[i+1] = alist[i+1], alist[i]
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

# 改进
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges :
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1