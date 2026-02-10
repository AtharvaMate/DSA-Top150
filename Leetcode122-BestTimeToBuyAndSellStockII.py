from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def fn(i, buy):
            if (i == n):
                return 0
            
            profit = 0

            if(buy):
                profit = max((-(prices[i])+fn(i+1,0)), (0+fn(i+1,1)))
            
            else:
                profit = max((prices[i]+fn(i+1,1)), (0+fn(i+1,0)))
            
            return profit
        return(fn(0,1))