#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = dict()

        for i, val in enumerate(nums):
            diff = target - val

            if diff in hmap:
                return [hmap[diff], i]
            
            hmap[val] = int
        
# @lc code=end

