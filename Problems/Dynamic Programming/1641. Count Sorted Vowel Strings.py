class Solution:
    def countVowelStrings(self, n: int) -> int:
        ar=[1]*5
        i=0
        while i<n-1:
            j=0
            while j<5:
                ar[j]=sum(ar[j:])
                j+=1
            i+=1
        return sum(ar)
