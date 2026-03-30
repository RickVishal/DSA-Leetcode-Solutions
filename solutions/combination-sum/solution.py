class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index,sum1,arr):
            if sum1==target:
                result.append(arr[:])
                return 
            if sum1>target:
                return 

            for i in range(index,len(candidates)):
                arr.append(candidates[i])
                backtrack(i,sum1+candidates[i],arr)
                arr.pop()

        result=[]
        backtrack(0,0,[])
        return result


        