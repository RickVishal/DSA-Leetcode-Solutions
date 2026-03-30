from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size=len(p)
        target=Counter(p)
        current=Counter(s[:size])
        result=[]
        if current==target:
            result.append(0)
        for i in range(size,len(s)):
            current[s[i]]+=1
            s_char=s[i-size]
            if current[s_char]==1:
                del current[s_char]
            else:
                current[s_char]-=1
            
            if target==current:
                result.append(i-size+1)

        return result


        

        