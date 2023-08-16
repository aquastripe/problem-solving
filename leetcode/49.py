import string
from collections import defaultdict
from typing import List

import pytest


def is_anagram(s: str, t: str) -> bool:
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)
    for string, dictionary in [(s, s_dict), (t, t_dict)]:
        for ch in string:
            dictionary[ch] += 1

    return s_dict == t_dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_character_occurrence(_strs):
            ch_counter = {ch: 0 for ch in string.ascii_lowercase}
            for ch in _strs:
                ch_counter[ch] += 1

            hashable_counter = [f'{ch}:{count}' for ch, count in ch_counter.items()]
            hashable_counter = ','.join(hashable_counter)
            return _strs, hashable_counter

        groups = defaultdict(list)
        strs_occurrences = list(map(count_character_occurrence, strs))
        for _strs, ch_counter in strs_occurrences:
            groups[ch_counter].append(_strs)
        groups = list(groups.values())
        return groups


@pytest.mark.parametrize(
    'strs,expected',
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_samples(strs, expected):
    solution = Solution()
    groups = solution.groupAnagrams(strs)
    is_all_anagrams = True
    for group in groups:
        for i in range(len(group) - 1):
            if not is_anagram(group[i], group[i + 1]):
                is_all_anagrams = False
                break

        if not is_all_anagrams:
            break

    assert is_all_anagrams
