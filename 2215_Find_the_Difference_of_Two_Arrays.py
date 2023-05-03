"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        answer = []
        answer.append(nums1.difference(nums2))
        answer.append(nums2.difference(nums1))
        return answer
    
"""
Complexity Analysis
The time complexity of the given solution is O(n), where n is the size of the larger input array since the set conversion takes O(n) time complexity, and set difference operation takes constant time complexity. 

The space complexity of the given solution is O(n), where n is the size of the larger input array. This is because we are creating two sets to store the input arrays, which can take up to O(n) space complexity. We are also creating a list to store the answer, which takes constant space complexity.
"""