class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=sum(list(map(int,str(num))))
        
        return num
