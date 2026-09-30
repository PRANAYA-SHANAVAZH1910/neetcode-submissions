class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen=prices[0]
        max_profit=0
        for i in prices:
            if i<lowest_seen:
                lowest_seen=i
            possible_profit=i-lowest_seen
            if possible_profit>max_profit:
                max_profit=possible_profit
        return max_profit