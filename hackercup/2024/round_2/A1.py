import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    peaks = []
    for n_digits in range(1, 18):
        if n_digits % 2 == 0:
            continue

        for n in range(1, 10):
            num = n
            m = n
            k = (n_digits - 1) // 2
            for i in range(1, k + 1):
                if m > 10:
                    break

                num *= 10
                num += m + 1
                m += 1

            if m == 10:
                break

            for i in range(k + 1, 2 * k + 1):
                num *= 10
                num += m - 1
                m -= 1

            peaks.append(num)

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
