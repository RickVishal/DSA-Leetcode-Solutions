class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,arr):
            result.append(arr[:])
            for i in range(start,len(nums)):
                arr.append(nums[i])
                backtrack(i+1,arr)
                arr.pop()

        result=[]
        backtrack(0,[])
        return result
        