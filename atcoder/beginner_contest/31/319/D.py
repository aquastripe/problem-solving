def is_valid(nums, num_lines_at_most, width) -> bool:
    num_lines = 1
    rest_width = width
    for num in nums:
        if num > width:
            return False

        if rest_width < num:
            rest_width = width
            num_lines += 1

        rest_width -= num + 1

    return num_lines <= num_lines_at_most


def binary_search(nums, m, lower_bound, upper_bound):
    if is_valid(nums, m, lower_bound):
        return lower_bound

    if not is_valid(nums, m, upper_bound):
        return -1

    while lower_bound + 1 != upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if is_valid(nums, m, mid):
            upper_bound = mid
        else:
            lower_bound = mid

    return upper_bound


def main():
    n, m = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))

    lower_bound = max(nums)
    upper_bound = sum(nums) + len(nums) - 1
    result = binary_search(nums, m, lower_bound, upper_bound)
    print(result)


if __name__ == '__main__':
    main()
