class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(index,sum1,arr):
            if len(arr)==k:
                if sum1==n:
                    result.append(arr[:])
                    return 
                if sum1>n:
                    return 
            for i in range(index,10):
                arr.append(i)
                backtrack(i+1,sum1+i,arr)
                arr.pop()

        result=[]
        backtrack(1,0,[])
        return result
        