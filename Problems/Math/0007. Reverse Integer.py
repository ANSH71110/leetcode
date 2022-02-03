class Solution:
    def reverse(self, x: int) -> int:
        tag=rev=0
        if x<0:
            x= -x
            tag=1
        while x:
            rev= rev*10 + x%10
            x//=10
        if tag==1:
            rev= -rev
        if rev>=-2147483648 and rev<=2147483647:
            return rev
        else:
            return 0
    
