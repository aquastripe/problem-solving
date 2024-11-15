import argparse
from itertools import combinations_with_replacement


def to_prefix(digits):
    num = digits[0]
    for digit in digits[1:]:
        num *= 10
        num += digit
    return num


def to_suffix(digits):
    digits = digits[::-1]
    return to_prefix(digits)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    peaks = []
    ten_multiples = [10 ** n for n in range(1, 11)]
    for n in range(1, 9):
        if n == 1:
            prefix_nums = list(range(1, 10))
            suffix_nums = prefix_nums
        else:
            monotonically_non_decreasing_digits = list(combinations_with_replacement(range(1, 9), n))
            prefix_nums = [to_prefix(digits) for digits in monotonically_non_decreasing_digits]
            suffix_nums = [to_suffix(digits) for digits in monotonically_non_decreasing_digits]

        for prefix_num in prefix_nums:
            for mid in range(2, 10):
                last_prefix_num = prefix_num % 10
                if last_prefix_num >= mid:
                    continue

                for suffix_num in suffix_nums:
                    n_suffix_digits = len(str(suffix_num))
                    first_suffix_num = int(str(suffix_num)[0])
                    if mid > first_suffix_num:
                        peak = (prefix_num * ten_multiples[n_suffix_digits] + mid * ten_multiples[n_suffix_digits - 1]
                                + suffix_num)
                        peaks.append(peak)

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            a, b, m = map(int, f_in.readline().split())
            ans = 0
            for peak in peaks:
                if a <= peak <= b and (peak % m) == 0:
                    ans += 1

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
