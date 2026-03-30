import numpy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        right=1
        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=left
            left*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=right
            right*=nums[i]

        return ans