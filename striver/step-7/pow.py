
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = (1/x)
        if n == 0:
            return 1
        return x * self.myPow(x,n-1)
        
print(Solution().myPow(0.00001,))