is_debug = False


def debug_message(num):
    if is_debug:
        if num:
            print('x' * num, end='')
        else:
            print()


def is_valid(nums, m, width) -> bool:
    num_lines = 1
    rest_in_line = width
    is_first_num = True
    for i, num in enumerate(nums):
        if num > width:
            return False

        if is_first_num:
            rest_in_line -= num
            is_first_num = False
            debug_message(num)
        else:
            if rest_in_line >= num + 1:
                # enough
                debug_message(num)
                rest_in_line -= num + 1

                if rest_in_line == 0 and (i + 1) < len(nums):
                    num_lines += 1
                    rest_in_line = width
                    is_first_num = True
                    debug_message(0)
                else:
                    is_first_num = False
            else:
                # not enough
                num_lines += 1
                rest_in_line = width
                debug_message(0)

                rest_in_line -= num
                debug_message(num)

    if num_lines > m:
        return False
    else:
        return True


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
