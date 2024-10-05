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
            a_b = [list(map(int, f_in.readline().split())) for _ in range(n)]
            t_a, t_b = a_b[0]
            if t_a == 0:
                t_a += 1e-6
            v_ub, v_lb = 1 / t_a, 1 / t_b
            for i in range(1, n):
                t_a, t_b = a_b[i]
                if t_a == 0:
                    t_a += 1e-6
                v_a, v_b = (i + 1) / t_a, (i + 1) / t_b
                # v_a > v_b
                if v_a < v_ub:
                    v_ub = v_a

                if v_b > v_lb:
                    v_lb = v_b

            if v_lb > v_ub:
                print(f'Case #{case + 1}: -1', file=f_out)
            else:
                ans = v_lb
                print(f'Case #{case + 1}: {ans:.6f}', file=f_out)


if __name__ == '__main__':
    main()
