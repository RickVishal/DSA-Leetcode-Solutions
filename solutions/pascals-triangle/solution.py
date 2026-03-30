class Solution:
    def pascal(self,row: int)->List[int]:
        ans=1
        list1=[]
        list1.append(1)
        for i in range(1,row):
            ans=ans*(row-i)
            ans=int(ans/(i))
            list1.append(ans)
        return list1
    def generate(self, numRows: int) -> List[List[int]]:
        list2=[]
        if numRows<=0:
            return []
        for i in range(1,numRows+1):
            list2.append(self.pascal(i))

        return list2
        
        




    