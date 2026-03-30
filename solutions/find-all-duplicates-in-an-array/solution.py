class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap={}
        l=[]
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for key,value in hashmap.items():
            if value>1:
                l.append(key)
        return l