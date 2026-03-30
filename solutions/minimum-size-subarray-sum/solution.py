class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        min_len=float('inf')
        c_sum=0
        while(r<len(nums)):
            c_sum+=nums[r]
            while(c_sum>=target):
                min_len=min(min_len,r-l+1)
                c_sum-=nums[l]
                l+=1
            r+=1
        return min_len if min_len!=float('inf') else 0
        