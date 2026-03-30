class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float(-inf)
        summ=0
        for i in range(len(nums)):
            summ=max(nums[i],summ+nums[i])
            max_sum=max(max_sum,summ)

        return int(max_sum)



        
        