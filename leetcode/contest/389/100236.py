class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        from collections import Counter

        counter = Counter(s)
        ans = 0
        for i in range(counter[c]):
            ans += i + 1

        return ans
