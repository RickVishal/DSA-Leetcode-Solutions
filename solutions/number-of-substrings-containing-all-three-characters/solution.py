class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        mapp={char:0 for char in 'abc'}
        count=0

        while(r<len(s)):
            if s[r] in mapp:
                mapp[s[r]]+=1
            while all(mapp[char]>0 for char in 'abc'):
        
                count+=len(s)-r
                if s[l] in mapp:
                    mapp[s[l]]-=1
                l+=1
            r+=1
        return count
        