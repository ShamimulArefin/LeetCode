# way 1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        x, y = 1, 2
        for i in range(2,n):
            step = x
            x = y
            y = step+y
        return y