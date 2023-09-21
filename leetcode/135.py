from typing import *

import pytest


def _two_loops_greedy(ratings):
    nums_greater_than_right = [1] * len(ratings)
    nums_greater_than_left = [1] * len(ratings)
    indices_from_left = list(range(1, len(ratings)))
    indices_from_right = reversed(list(range(len(ratings) - 1)))

    for i in indices_from_left:
        if ratings[i] > ratings[i - 1]:
            nums_greater_than_left[i] = nums_greater_than_left[i - 1] + 1

    for i in indices_from_right:
        if ratings[i] > ratings[i + 1]:
            nums_greater_than_right[i] = nums_greater_than_right[i + 1] + 1

    total = 0
    for i in range(len(ratings)):
        total += max(nums_greater_than_left[i], nums_greater_than_right[i])

    return total


class Solution:
    def candy(self, ratings: List[int]) -> int:
        return _two_loops_greedy(ratings)


@pytest.mark.parametrize(
    'ratings,expected',
    [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 2, 87, 87, 87, 2, 1], 13),
        ([29, 51, 87, 87, 72, 12], 12),
        ([1, 6, 10, 8, 7, 3, 2], 18),
    ],
)
def test_samples(ratings, expected):
    solution = Solution().candy(ratings)
    assert solution == expected
