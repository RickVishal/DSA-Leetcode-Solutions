from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def goalatmost(goal):
            if goal<0:
                return 0
            left = 0
            sum1 = 0
            count = 0

            for right in range(len(nums)):
                sum1 += nums[right]  

                
                while sum1 > goal and left <= right:
                    sum1 -= nums[left]
                    left += 1

          
                count+=(right-left+1)
        
            return count
        return goalatmost(goal)-goalatmost(goal-1)

   
