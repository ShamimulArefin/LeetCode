# way 1 normal math
class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n*n<=x:
            n+=1
        return n-1

# way 2 binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while right>=left:
            mid = (left + right)//2
            if mid*mid<=x:
                left = mid+1
            else:
                right = mid-1   
                    
        return right