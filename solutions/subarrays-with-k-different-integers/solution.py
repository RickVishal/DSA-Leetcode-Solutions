class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            l=0
            r=0
            count=0
            freq={i:0 for i in nums}
            for r in range(len(nums)):
                if freq[nums[r]]==0:
                    k-=1
                freq[nums[r]]+=1
                while k<0:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        k+=1
                    l+=1

                count+=r-l+1
            return count
        return atmost(k)-atmost(k-1)

        


        