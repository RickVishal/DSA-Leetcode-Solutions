class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        if not arr:
            return 0
        arr=sorted(set(arr))
        count=1
        max_length=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]+1:
                count+=1
            else:
                max_length=max(max_length,count)
                count=1
            
        return max(max_length,count)