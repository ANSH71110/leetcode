class Solution:
    def fib(self, n: int) -> int:
        f=[0,1]
        i=2
        if n>=2:
            while i<=n:
                f.append(f[i-1]+f[i-2])
                i+=1
        return f[n]
            
