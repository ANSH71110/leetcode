class Solution:
    def reformat(self, s: str) -> str:
        s1=''
        d=''
        i=0
        while i<len(s):
            if ord(s[i])<80:
                d+=s[i]
            else:
                s1+=s[i]
            i+=1
        str=''
        if abs(len(d)-len(s1))<2:
            i=0
            j=0
            tag=0
            if len(d)>len(s1):
                j+=1
                str+=d[0]
            elif len(s1)>len(d):
                tag=1
                i+=1
                str+=s1[0]
            
            while j<len(d):
                if tag==0:
                    str+=s1[i]+d[j]
                else:
                    str+=d[j]+s1[i]                    
                i+=1
                j+=1        
        
        return str
