class Solution:
    def isValid(self, s: str) -> bool:
        count=0
        stack=[]
        if len(s)<=1:
            return False
        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)

            elif not stack or (ch==")" and stack[-1]!="(") or (ch=="}" and stack[-1]!="{") or (ch=="]" and stack[-1]!="["):
                return False
            else:

                stack.pop()
        return True if not stack else False
         
            
        