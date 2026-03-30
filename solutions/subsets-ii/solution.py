class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index,arr):
            result.append(arr[:])
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                backtrack(i+1,arr)
                arr.pop()
        result=[]
        nums.sort()
        backtrack(0,[])
        return result