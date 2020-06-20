"""参考: https://www.jianshu.com/p/cdfa79919c9b
活动安排问题-贪心算法

1.问题:
假定有一个n个活动的集合S={a[1], a[2], ..., a[n]}, 这些活动使用相同的资源(例如一个阶梯教室)，
而这些资源在某个时刻只能供一个活动使用. 每个资源都有以个开始时间s[i]和结束时间 f[i] 且0 <= s[i] < f[i].
求最大兼容活动集(活动a[i]和活动a[j]满足 s[i] <= a[i] < fi 和 s[j] <= a[j] < f[j] 不重叠)
即: 所求的是一个原本全集的子集

2.子问题:
令A[i, j]是所求S[i, j]的最优解, 包含活动a[k], 最优解包含活动a[k],则得到两个子问题:
    S[i, k]和S[k, j] 所求 A[i, j] = A[i, k] U {a[k]} U A[k, j]

3.贪心选择
选择一个活动使得选出它后, 剩下的资源能被尽量多的其他任务所用.
直觉: 选择S中最早结束的活动, 因为它剩下的资源可供它之后尽量多的活动使用.
令S[k] = {a[i] 属于 S:s[i] >= f[k]} 为在a[k]结束后开始的任务集合, 做出贪心选择(选出a1)后, 剩下的S1是唯一
需要求解的子问题.
"""
L = []


def eventRecursion(s, f, k, n):
    """递归贪心算法
    核心算法: 
    先把活动按照时间开始从小到大排序,
    在找出最大相容的活动安排集合
    :param s: list[], 活动开始的时间
    :param f: list[], 活动结束的时间
    :param k: k, 指出要求解的子问题Sk
    :param n: 问题规模n
    :return:  返回Sk的一个最大兼容活动集
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        L.append(m)
        eventRecursion(s, f, m, n)
        return L
    else:
        return

def activity(s, f):
    n = len(s)
    result = [1]
    k=1
    tempList = list(range(n))
    tempList = tempList[2:]
    for m in tempList:
        if s[m] >= f[k]:
            result.append(m)
            k = m
    return result

print(eventRecursion([0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12], [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16], 0, 11))
# print(activity([0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12], [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]))
'''
结果:[1,4,8,11]
'''