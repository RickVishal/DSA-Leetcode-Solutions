class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in nmap:
                return [nmap[diff],i]
            nmap[num]=i
        return []
        