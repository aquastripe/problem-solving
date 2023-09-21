from typing import *

import pytest


def reverse_nums_from(nums, i):
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the longest decreasing sequence
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # find the pivot
        pivot = i - 1
        if pivot >= 0:
            # find the successor from the end
            j = len(nums) - 1
            while nums[j] <= nums[pivot]:
                j -= 1

            successor = j

            # swap the pivot and the successor
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

            # reverse the sequence after the successor
            reverse_nums_from(nums, pivot + 1)
        else:
            reverse_nums_from(nums, 0)


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 1], [1, 1]),
        ([1, 3, 2], [2, 1, 3]),
    ],
)
def test_samples(nums, expected):
    Solution().nextPermutation(nums)
    assert nums == expected
