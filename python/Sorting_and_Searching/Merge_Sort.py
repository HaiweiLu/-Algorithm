def mergeSort(alist):
    '''
    思路：  归并排序是递归算法，思路是将数据表分裂成两半，
            对两半分别进行归并排序
    递归的基本结束条件是：数据表仅有1个数据项，自然是排好序的
    缩小规模：将数据表分裂为相等的两半，规模减小为原来的二分之一
    调用自身：将两半分别调用自身排序，然后将分别排好序的两半进行归并，得到排好序的数据表
    '''
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[: mid]
        righthalf = alist[mid :]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    #print("Merging ", alist)

# 另一个归并排序代码(老司机)，充分利用了列表的特点
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = int(len(lst) / 2)
    left = merge_sort(lst[: middle])
    right = merge_sort(lst[middle :])
    merged = []

    while left and right:

        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        
    merged.extend(right if right else left)
    

    '''
    # 把上面的 while 循环详细写的版本
    while len(left) > 0 and len(right) > 0:
        
        if left[0] > right[0]:
            merged.append(right.pop(0))
        else:
            merged.append(left.pop(0))
        
    merged.extend(left + right)
    '''

    return merged

alist = [54, 26, 93, 44, 56, 88, 77, 21, 90]
#mergeSort(alist)
#print(alist)
lst = merge_sort(alist)
print(lst)

'''
写代码时犯的错误，
错误代码： merged.append(right.pop[0])
报错 TypeError: 'builtin_function_or_method' object is not subscriptable

解决办法，改为 merged.append(right.pop(0))，即可
'''