"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# way 1
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product>0:
                return 1
            elif product<0:
                return -1
            else:
                return 0
        product = 1
        for i in nums:
            product *= i
        return signFunc(product)

# way 2
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        m = 1
        for i in nums:
            m *= i
        if m>0:
            return 1
        elif m<0:
            return -1
        else:
            return 0