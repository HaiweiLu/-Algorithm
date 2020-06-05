'''
参考资料 
https://segmentfault.com/a/1190000014906917
https://www.cnblogs.com/Pinging/p/7852469.html

给定一个1~N 连续整数集合, 问分割为两个和相等的子集,
可以有多少种分割方式 ?

动态转移方程:
原集合 arr = [1, ..., n]

if j >= arr[i - 1]:
    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
else:
    dp[i][j] = dp[i - 1][j]
'''

def splitSubset(n):
    Sum = (n + 1) * n / 2
    target = int(Sum / 2 + 1)
    if Sum % 2: # 集合和如果为奇数,就无法分割出两个和相等的子集
        return 0

    dp = [[0] * (target) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(target):
            if i <= j:
                dp[i][j] = dp[i-1][j-i] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target-1] / 2 # 计数过程有重复计算的


if __name__ == "__main__":
    n = 7
    print("split subset: {}".format(splitSubset(n)))