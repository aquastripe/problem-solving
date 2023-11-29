def is_different_parity_in_adjacent_elements(nums, i, target_num):
    return i == 0 or nums[i - 1] % 2 != target_num % 2


def dfs(nums, i, n, is_used):
    if i == n:
        print(' '.join(map(str, nums)))
        return

    for target_num in range(1, n + 1):
        if not is_used[target_num] and is_different_parity_in_adjacent_elements(nums, i, target_num):
            is_used[target_num] = True
            nums.append(target_num)
            dfs(nums, i + 1, n, is_used)
            # back-tracking
            is_used[target_num] = False
            nums.pop()


def main():
    n = 4
    nums = []
    is_used = [False] * (n + 1)
    dfs(nums, 0, n, is_used)


if __name__ == '__main__':
    main()
