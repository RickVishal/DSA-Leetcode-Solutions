class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap={}
        output=0
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        for k,v in hmap.items():
            if v>1:
                output=k
        return output 
                
        