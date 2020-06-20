"""
贪心算法实现背包问题

问题:

假设有一个贪婪的小偷, 背有一个可装 c kg 的重东西的背包,
在商场伺机盗窃各种可以装进背包的商品.

使用贪心策略:
items: 物品的信息(价值和重量)
contains: 背包容量
maxValue = 0
for value, weight -> items:
    if weight <= contains:
        maxValue += value
        contains -= weight
    end
end
return maxValue
"""

def KnapSack(items, contains):
    """完全背包问题贪心算法解法
    算法核心:
    优先拿取 价值/重量 最大的物品,直到背包放不下

    Args:
        items ([(价值, 重量)]): 物品信息
        contains (int): 背包容量

    Returns:
        int: 找到的最大价值
    """
    maxValue = 0
    for value, weight in items:
        if weight <= contains:
            maxValue += value
            contains -= weight
    return maxValue


if __name__ == "__main__":
    # items [(物品价值, 物品重量)]: 为物品信息列表
    items = [(20, 10), (60, 10), (100, 20), (120, 30)]
    # 把物品的信息按照单位重量的价值排序, value / weight
    items = sorted(items, key = lambda x : (x[0] /  x[1]), reverse = True)
    packContains = 10
    maxValue = KnapSack(items, packContains)
    print(maxValue)