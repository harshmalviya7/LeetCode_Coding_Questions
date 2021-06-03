# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices: List[int]) -> int:
    minimum = 100000
    maximum = 0
    for i in prices:
        minimum = min(minimum, i)
        maximum = max(maximum, i - minimum)

    return maximum

print(maxProfit([7,1,5,3,6,4]))  #5

# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
def maxProfit(self, prices: List[int]) -> int:
    a = 0
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            a += prices[i] - prices[i - 1]

    return a


print(maxProfit([7,1,5,3,6,4])) #7