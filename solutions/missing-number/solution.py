class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_of=n*(n+1)//2
        actual_sum=sum(nums)
        return sum_of-actual_sum

        