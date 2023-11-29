from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        new_nums = []
        indices = []
        is_used = [False] * len(nums)

        def dfs(i):
            if i == len(nums):
                new_nums.append([nums[j] for j in indices])
                return

            for j in range(len(nums)):
                if is_used[j]:
                    continue

                is_used[j] = True
                indices.append(j)
                dfs(i + 1)
                is_used[j] = False
                indices.pop()

        dfs(0)

        return new_nums
