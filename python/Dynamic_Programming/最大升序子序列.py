'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

说明:
    可能会有多种最长上升子序列的组合,只需输出对应长度即可
'''

def lengthOfLIS(nums):
    if len(nums) <= 1:
        return len(nums)

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    nums = [5, 8, 9, 2, 3, 1, 7, 4, 6]
    print("max length of LIS: {}".format(lengthOfLIS(nums)))