import argparse
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            n = f_in.readline()
            s = list(f_in.readline())
            s = list(map(int, s[:-1]))

            q = f_in.readline()[:-1]
            q = int(q)
            pressed = defaultdict(int)
            for _ in range(q):
                b_i = int(f_in.readline())
                pressed[b_i] += 1

            for b_i, count in pressed.items():
                if count % 2 == 1:
                    for i in range(b_i - 1, len(s), b_i):
                        s[i] = 1 - s[i]

            ans = 0
            for i, c in enumerate(s):
                if c == 1:
                    ans += 1
                    for j in range(i, len(s), i + 1):
                        s[j] = 1 - s[j]

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
