# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:26:34 2019

@author: haiwe

#二分查找
"""
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last)//2  #求商
        if alist[midpoint] == item:   #中间项对比
            found = True
        else:                    #缩小对比范围
            if item < alist[midpoint]: #如果所找在中间项左边，调整查找范围，缩小右边
                last = midpoint-1
            else:                #如果所找项在中间项右边，则调整左边
                first = midpoint+1
                
    return found

#分而治之（递归）
def BinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return BinarySearch(alist[:midpoint],item)
            else:
                return BinarySearch(alist[midpoint+1:],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print(BinarySearch(testlist, 3))
print(BinarySearch(testlist, 13))

