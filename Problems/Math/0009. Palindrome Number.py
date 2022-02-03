class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=x1=0
        if x>=0:        
            x1=x
            while x:
                rev=rev*10 + x%10
                x//=10
            if rev==x1:
                return 1
        
        else:
            return 0
