from typing import *

import pytest


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        num = 0
        prefix_sum = [0] * len(boxes)
        prefix_sum[0] = boxes[0] == '1'
        suffix_sum = [0] * len(boxes)
        for i in range(1, len(boxes)):
            prefix_sum[i] = prefix_sum[i - 1] + (boxes[i] == '1')
            suffix_sum[-(i + 1)] = suffix_sum[-i] + (boxes[-i] == '1')
            num += i * (boxes[i] == '1')

        ans.append(num)
        for i in range(1, len(boxes)):
            num += prefix_sum[i - 1] - suffix_sum[i - 1]
            ans.append(num)

        return ans


@pytest.mark.parametrize(
    'boxes,expected',
    [
        ("110", [1, 1, 3]),
        ("001011", [11, 8, 5, 4, 3, 4]),
    ],
)
def test_samples(boxes, expected):
    solution = Solution().minOperations(boxes)
    assert solution == expected
