class Solution:
    def frequencySort(self, s: str) -> str:
       
        hashmap={i:0 for i in s}
        for i in s:
            hashmap[i]+=1
        l=[]    
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))    
        for key,value in hashmap.items():
            for j in range(value):
                l.append(key)
        return "".join(l)
        
        