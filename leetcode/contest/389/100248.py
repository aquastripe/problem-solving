class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        t = s[::-1]
        for i in range(n - 1):
            if t.find(s[i:i + 2]) != -1:
                return True
        else:
            return False
