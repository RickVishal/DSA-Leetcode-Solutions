class Solution:
    def isPalindrome(self, s: str) -> bool:
        l1=list(s)
        clean="".join([i.lower()for i in l1 if i.isalnum()])
        reverse=clean[::-1]
        return clean==reverse
        

        