from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i1, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in num_to_index:
                i2 = num_to_index[n2]
                return [i1, i2]

            num_to_index[n1] = i1

        return None


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_samples(nums, target, expected):
    solution = Solution().twoSum(nums, target)
    assert set(solution) == set(expected)
