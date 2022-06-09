class Solution:
    def defangIPaddr(self, address: str) -> str:
        i=0
        s=''
        while i<len(address):
            if address[i]=='.':
                s+='[.]'
            else:
                s+=address[i]
            i+=1
        return s
