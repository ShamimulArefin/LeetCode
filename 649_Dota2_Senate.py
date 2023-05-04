"""
way 1
The time complexity of the algorithm is O(N^2), where N is the length of the input string senate. This is because the algorithm uses nested loops to iterate over the senate string and the lists r and d.

Space Complexity:
The space complexity of the algorithm is O(N), where N is the length of the input string senate. This is because the algorithm uses two lists r and d to store the indices of the senators. The length of these lists can be at most N/2, which gives us a space complexity of O(N).
"""

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = [], []   
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        i, st = len(senate)+1, ''
        while True:
            if len(r) == 0 and len(d) != 0:
                st = 'Dire'
                break
            elif len(r) != 0 and len(d) == 0:
                st = 'Radiant'
                break
            if r[0] < d[0]:
                r.remove(r[0])
                d.remove(d[0])
                r.append(i)
                i += 1
            else:
                r.remove(r[0])
                d.remove(d[0])
                d.append(i)
                i += 1
        
        return st