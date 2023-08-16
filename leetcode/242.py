import pytest
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for string, dictionary in [(s, s_dict), (t, t_dict)]:
            for ch in string:
                dictionary[ch] += 1

        return s_dict == t_dict


@pytest.mark.parametrize(
    's,t,expected',
    [
        ('anagram', 'nagaram', True),
        ('rat', 'car', False),
    ],
)
def test_samples(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected
