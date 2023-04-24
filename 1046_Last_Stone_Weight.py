# way 1
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones)==1:
                break
            elif len(stones)==2:
                if stones[0]==stones[1]:
                    stones[0] = 0
                    break
                else:
                    mx, mn = max(stones[0], stones[1]), min(stones[0], stones[1])
                    stones.remove(mn)
                    stones[0] = mx - mn
                    break
            else:
                stones.sort()
                x, y = stones[-1], stones[-2]
                if x==y:
                    stones.remove(x)
                    stones.remove(y)
                else:
                    mx, mn = max(x,y), min(x, y)
                    stones.remove(mn)
                    stones[-1] = mx-mn
        return stones[0]

"""
Complexity

Time complexity: O(n^2)
Space complexity: O(1)

Description

The time complexity of this code is O(n^2) in the worst case where n is the length of the input list stones. This is because the sort() method used in the else block has a worst-case time complexity of O(nlogn), and it is being called within a while loop that can iterate up to n times. Therefore, the time complexity of the sort operation inside the while loop is O(nlogn), and the time complexity of the while loop itself is    O(n). The overall time complexity of the code is the product of these two, which is O(n^2) in the worst case.

The space complexity of this code is O(1), which is constant space complexity. This is because the input list stones is modified in place without creating any new lists or data structures, so the space required by the algorithm remains constant regardless of the size of the input list. The only additional space used by the algorithm is for a constant number of variables such as x, y, mx, and mn, which do not depend on the size of the input list.
"""