class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dummy = []
        i = 0
        j =0
        while i < len(prices):
            j = i +1
            while j < len(prices):
                aa = prices[j] - prices[i]
                if aa > 0:
                    dummy.append(aa)
                j = j +1
            i = i +1

        if dummy:
            return max(dummy)
        return 0


            
