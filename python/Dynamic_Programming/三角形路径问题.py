'''
三角形矩阵, 找到从顶到底的最小路径和最大路径
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import copy

def findPath(triangle):
    minPathDp = copy.deepcopy(triangle) # 复制一份数据,用于存储每一次动态规划的结果
    maxPathDp = copy.deepcopy(triangle)

    for i in range(len(triangle) - 1, 0, -1): # 自底向上
        for j in range(i):
            minPathDp[i-1][j] += min(triangle[i][j], triangle[i][j+1])
            maxPathDp[i-1][j] += max(triangle[i][j], triangle[i][j+1])

    minPath = [triangle[0][0]] # 最小和路径
    maxPath = [triangle[0][0]] # 最大和路径

    for i in range(1, len(triangle)): # 回溯找到最优的路径
        Min, minNumberIndex = minPathDp[i][0], 0
        Max, maxNumberIndex = maxPathDp[i][0], 0
        for j in range(i + 1):
            if Min > minPathDp[i][j]:
                Min, minNumberIndex = minPathDp[i][j], j
            if Max < maxPathDp[i][j]:
                Max, maxNumberIndex = maxPathDp[i][j], j
        
        minPath.append(triangle[i][minNumberIndex])

        maxPath.append(triangle[i][maxNumberIndex])
    
    for row in minPathDp:
        print(row)
    print("=========")
    for row in maxPathDp:
        print(row)
    
    return minPath, minPathDp[0][0], maxPath, maxPathDp[0][0]

if __name__ == "__main__":
    triangle = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    minPath, minPathSum, maxPath, maxPathSum = findPath(triangle)
    print("minPath: {}, minPathSum: {}, maxPath: {}, maxPathSum: {}" \
        .format(minPath, minPathSum, maxPath, maxPathSum))