from typing import List

import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)

        return False


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
)
def test_samples(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
