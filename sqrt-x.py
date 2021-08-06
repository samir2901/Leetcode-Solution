class Solution:
    def mySqrt(self, x: int) -> int:
        xi = x 
        precision = 0.00001
        while abs(x - xi*xi) > precision:
            xi = (xi + x/xi)/2
            print("xi=",xi)
        return int(xi) 

sol = Solution() 
print("Ans=",sol.mySqrt(8))
        