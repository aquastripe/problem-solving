from typing import *

import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        count_characters = defaultdict(int)
        max_length = 0
        i = -1
        for j, c in enumerate(s):
            count_characters[c] += 1
            while count_characters[c] > 1:
                i += 1
                count_characters[s[i]] -= 1
            else:
                max_length = max(max_length, j - i)

        return max_length


@pytest.mark.parametrize(
    's,expected',
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        (' ', 1),
        ('', 0),
        ('aab', 2),
    ],
)
def test_samples(s, expected):
    solution = Solution().lengthOfLongestSubstring(s)
    assert solution == expected
