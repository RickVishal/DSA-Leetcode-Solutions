class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            l=0
            count=0
            for r in range(len(nums)):
                if nums[r]%2!=0:
                    k-=1
                while(k<0):
                    if nums[l]%2!=0 and l<=r:
                        k+=1
                    l+=1
                count+=(r-l+1)

            return count
        return at_most_k(k)-at_most_k(k-1)

    


        

    
   
            
        