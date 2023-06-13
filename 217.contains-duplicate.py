#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def merge(nums):
            if len(nums) > 1:
                left = nums[:len(nums)//2]
                right = nums[len(nums)//2:]

                merge(left)
                merge(right)


                i = 0
                j = 0
                k = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1

                    else:
                        nums[k] = right[j]
                        j += 1

                    k += 1

                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1

        merge(nums)
        print(nums)

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
# @lc code=end

