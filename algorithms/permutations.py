def permutations(nums, i, n, is_used):
    if i == n:
        print(' '.join(map(str, nums)))
        return

    for target_num in range(1, n + 1):
        if is_used[target_num]:
            continue

        is_used[target_num] = True
        nums.append(target_num)
        permutations(nums, i + 1, n, is_used)
        is_used[target_num] = False
        nums.pop()


def main():
    n = 3
    nums = []
    is_used = [False] * (n + 1)
    permutations(nums, 0, n, is_used)


if __name__ == '__main__':
    main()
