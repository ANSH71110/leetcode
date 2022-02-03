class Solution:
    def romanToInt(self, s: str) -> int:
        dic={}
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=vc=vn=0
        sum=0
        while i<len(s):
            vc=dic[s[i]]
            if i<len(s)-1:
                vn=dic[s[i+1]]
                if vn<=vc:
                    sum+=vc
                    i+=1
                else:
                    sum+=(vn-vc)
                    i+=2
            else:
                sum+=vc
                i+=1
        return sum
