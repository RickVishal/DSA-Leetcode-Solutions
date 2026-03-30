class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        rev=x[::-1]
        if rev==x:
            return True
        else:
            return False
        
        
        