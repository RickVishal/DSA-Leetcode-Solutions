class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(current,open_count,close_count):
            if len(current)==2*n:
                result.append(current)
                return 
            if open_count<n:
                backtracking(current+"(",open_count+1,close_count)

            if close_count<open_count:
                backtracking(current+")",open_count,close_count+1)

        result=[]
        backtracking("",0,0)
        return result
        