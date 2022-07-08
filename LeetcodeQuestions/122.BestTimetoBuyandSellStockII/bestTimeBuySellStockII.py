def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    i = len(prices) - 1
    sum = 0
    while i > 0:
        if prices[i] > prices[i-1]:
            sum += prices[i] - prices[i-1]
        i -= 1
    return sum

# runtime beats 77.12%
# memory usage beats 67.44%
