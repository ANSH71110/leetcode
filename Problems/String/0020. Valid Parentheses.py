class Solution:
        def isValid(self,s: str) -> bool:
            l=[]
            obj=''
            i=j=0
            n=len(s)
            dict={'[':']','{':'}','(':')'}
            if n>=2:
                while i<n:
                    if s[i] in dict:
                        l.append(s[i]) 
                    else:
                        if len(l)>0:
                            s1=l.pop()
                            if dict[s1]!=s[i]:
                                return 0
                        else:
                            return 0
                    i+=1
                if len(l)==0:
                    return 1
                else:
                    return 0
            else:
                return 0
