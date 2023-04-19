# way 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                        if nums[i]+nums[j]==target:
                                lst.append([i, j])
        return lst[-1]
    
# way 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i ]
            lookup[num] = i

# way 3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                        if nums[i]+nums[j]==target:
                                return [i, j]

# way 4 in C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sz = nums.size();
            for(int i=0; i<sz-1; i++)
            {
                    for(int j=i+1; j<sz; j++)
                    {
                            if(nums[i]+nums[j] == target)
                            {
                                    return{i, j};
                            }
                    }
            }
            return {};
    }
};