class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        max_length=0
        zeroes=0
        while(r<len(nums)):
            if nums[r]==0:
                zeroes+=1
            
            if zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            if zeroes<=k:
                max_length=max(max_length,r-l+1)
            r+=1
        return max_length
        