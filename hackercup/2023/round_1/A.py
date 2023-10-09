import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            n = int(f_in.readline())
            x = list(map(int, f_in.readline().split()))
            x.sort()

            if n == 5:
                mid_a1 = (x[0] + x[1]) / 2
                mid_b1 = (x[-1] + x[-3]) / 2

                mid_a2 = (x[0] + x[2]) / 2
                mid_b2 = (x[-1] + x[-2]) / 2

                ans = max(mid_b1 - mid_a1, mid_b2 - mid_a2)
            else:
                mid_a = (x[0] + x[1]) / 2
                mid_b = (x[-1] + x[-2]) / 2
                ans = mid_b - mid_a

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
