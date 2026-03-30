class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        ans=1
        list1=[]
        list1.append(1)
        for i in range(1,rowIndex):
            ans=ans*(rowIndex-i)
            ans=int(ans/(i))
            list1.append(ans)
        return list1