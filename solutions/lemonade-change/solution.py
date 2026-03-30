class Solution:
    def lemonadeChange(self, arr: List[int]) -> bool:
        five=0
        ten=0
        for bill in arr:
            if bill==5:
                five+=1
            elif bill==10:
                if (five>0):
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if (five>0 and ten>0):
                    five-=1
                    ten-=1
                elif(five>=3):
                    five-=3
                else:
                    return False
        return True
        