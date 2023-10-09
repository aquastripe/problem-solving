import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            ans = ...

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
