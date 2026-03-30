class Solution:
    def jump(self, nums: List[int]) -> int:
        l=0
        r=0
        jumps=0
        while(r<len(nums)-1):
            jumps+=1
            far=0
            for i in range(l,r+1):
                far=max(i+nums[i],far)
            l=r+1
            r=far
            
        return jumps
        