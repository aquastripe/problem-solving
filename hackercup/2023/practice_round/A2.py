# Wrong Answer
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        t = int(f_in.readline())
        for i in range(1, t + 1):
            a, b, c = tuple(map(int, f_in.readline().split()))
            k_from_x_intercept = (2 * c) // b - 1
            k_from_y_intercept = c // a
            k_from_point_of_intersection = 2 * (c - a) // b + 1
            k = max(k_from_x_intercept, k_from_y_intercept, k_from_point_of_intersection)

            f_out.write(f'Case #{i}: {k}\n')


if __name__ == '__main__':
    main()
