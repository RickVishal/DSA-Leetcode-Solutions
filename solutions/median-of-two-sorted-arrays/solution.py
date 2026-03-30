class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
       
        p=len(nums1)
        
        mid=p/2
        if p%2!=0:
            mid=math.ceil(mid)
            midi=nums1[mid-1]
            
        else:
            mid=math.ceil(mid)
            midi=(nums1[mid]+nums1[mid-1])/2.0
            
        return midi
        