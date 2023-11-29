from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        new_nums = []

        def _permute(nums, i, n):
            if i == n:
                new_nums.append(list(nums))
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                _permute(nums, i + 1, n)
                nums[i], nums[j] = nums[j], nums[i]

        _permute(nums, 0, len(nums))
        return new_nums
