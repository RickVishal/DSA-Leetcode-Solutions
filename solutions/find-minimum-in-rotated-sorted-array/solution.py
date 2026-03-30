class Solution:
    def findMin(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        mid=0
        while(l<r):
            if arr[l] < arr[r]:
                return arr[l]
            mid=l+(r-l)//2
            if arr[mid]>arr[r]:
                l=mid+1
            elif arr[mid]<arr[r]:
                r=mid
        return arr[l]


        