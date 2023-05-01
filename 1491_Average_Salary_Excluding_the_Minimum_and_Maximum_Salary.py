"""
way 1
Time O(n)
Space O(1)
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary))/(len(salary)-2)


"""
way 2
Time O(nlogn)
Space O(1)
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary)/len(salary)