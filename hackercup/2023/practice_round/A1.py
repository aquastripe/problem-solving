import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        t = int(f_in.readline())
        for i in range(1, t + 1):
            s, d, k = tuple(map(int, f_in.readline().split()))
            num_patties_cheese_provided = 1 * s + 2 * d
            num_patties_cheese_needed = k
            num_buns_provided = 2 * s + 2 * d
            num_buns_needed = k + 1
            ans = 'YES' \
                if num_patties_cheese_provided >= num_patties_cheese_needed and num_buns_provided >= num_buns_needed \
                else 'NO'
            f_out.write(f'Case #{i}: {ans}\n')


if __name__ == '__main__':
    main()
