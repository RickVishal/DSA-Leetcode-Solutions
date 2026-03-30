class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        r=0
        l=0
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        while(l<m and r<n):
            if(g[r]<=s[l]):
                r+=1
            l+=1

        return r
        