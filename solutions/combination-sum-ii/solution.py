class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index,sum1,arr):
            if sum1==target:
               
                result.append(arr[:])
                    
                return
                
            if sum1>target:
                return 
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1,sum1+candidates[i],arr)
                arr.pop()
        result=[]
        candidates.sort()
        backtrack(0,0,[])
        return result
        