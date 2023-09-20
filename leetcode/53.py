from typing import *

import pytest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self._kadane_algorithm(nums)

    def _kadane_algorithm(self, nums):
        curr_max_sum = nums[0]
        total_max_sum = curr_max_sum
        for i in range(1, len(nums)):
            curr_max_sum = max(nums[i], curr_max_sum + nums[i])
            total_max_sum = max(total_max_sum, curr_max_sum)
        return total_max_sum


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-2, -1], -1),
    ],
)
def test_samples(nums, expected):
    solution = Solution().maxSubArray(nums)
    assert solution == expected
