class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum=0
        i=0
        while i<len(s):
            t=ord(s[i])-96
            sum+=t%10+t//10
            i+=1
        #print(sum)
        i=1
        while i<k:
            if sum//10==0:
                return sum
            else:
                s=0
                while sum>0:
                    s+=sum%10
                    sum//=10
                sum=s
            i+=1
        return sum
