'''
动态规划 投资问题
参考资料
https://segmentfault.com/a/1190000022360607
http://www.omica.com.cn/news/show-8723.html
'''
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1


def investDistribute(project, money):
    m, n = len(project), len(project[0])
    dp = [[0] * n for _ in range(m)]
    notebook = [[0] * n for _ in range(m)]

    for i in range(m): # 遍历项目
        for j in range(money + 1): # 对项目可以投钱的范围
            for k in range(j + 1): # 对项目具体投资 k 元
                if i == 0 and j != 0:
                    dp[i][j] = project[i][j]
                    notebook[i][j] = j
                elif dp[i][j] < project[i][k] + dp[i-1][j-k]:
                    dp[i][j] = project[i][k] + dp[i-1][j-k]
                    notebook[i][j] = k
    
    # for alist in dp:
    #     print(alist)
    # print("=========")
    # for row in notebook:
    #     print(row)
    traceback(notebook, m, money)
    return dp[-1][-1]

def traceback(notebook, projectNumber, money):
    if projectNumber <= 0 or money <= 0:
        return
    invest = notebook[projectNumber-1][money]
    print("project {}, invest {}".format(projectNumber, invest))

    traceback(notebook, projectNumber-1, money-invest)

def getInvest(project, money):
    
    if project is None or money <=0:
        return
    
    m, n = len(project), len(project[0])
    dp = [[0] * n for _ in range(m)]
    notebook = [[0] * n for _ in range(m)]

    for i in range(1, n):
        dp[0][i] = project[0][i]
        notebook[0][1] = 1

    for i in range(1, m):
        for j in range(money + 1):
            Max = 0
            for k in range(j + 1):
                if project[i][k] + dp[i-1][j-1] > Max:
                    Max = project[i][k] + dp[i-1][j-1]
                    notebook[i][j] = k
            dp[i][j] = Max

    print("=========")
    for row in dp:
        print(row)
    print("----------")
    for row in notebook:
        print(row)

if __name__ == "__main__":
    project = [[0, 15, 28, 40, 51], # project[i][j] 表示项目 i,投资 j 元的收益
                [0, 13, 29, 43, 55],
                [0, 11, 30, 45, 58]]
    money = 4
    project1 = [[0, 11, 12, 13, 14, 15],
                [0, 0, 5, 10, 15, 20],
                [0, 2, 10, 30, 32, 40],
                [0, 20, 21, 22, 23, 24]]
    print("MaxProfit: {}".format(investDistribute(project, money)))
    # print("MaxProfit: {}".format(investDistribute(project1, money + 1)))
    # getInvest(project, money)

    # coins = [1, 2, 5]
    # amount = 11
    # coinChange(coins, amount)