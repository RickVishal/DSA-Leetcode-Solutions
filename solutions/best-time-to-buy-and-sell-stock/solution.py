class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        min_price=float('inf')
        max_profit=0
        for i in range(len(arr)):
            if arr[i]<min_price:
                min_price=arr[i]
            if arr[i]-min_price>max_profit:
                max_profit=arr[i]-min_price
        return max_profit

        