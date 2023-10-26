import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            nr, nc = list(map(int, f_in.readline().split()))
            board = []
            for _ in range(nr):
                board.append(list(f_in.readline()[:-1]))

            ans = False
            for r in range(nr):
                for c in range(nc):
                    if board[r][c] == 'W':
                        board[r][c] = 'x'
                        stack = [(r, c)]
                        n_empty_spaces = 0
                        is_visited = np.zeros((nr, nc), dtype=bool)

                        while len(stack) > 0:
                            curr_r, curr_c = stack.pop()
                            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                next_r = curr_r + dr
                                next_c = curr_c + dc
                                if 0 <= next_r < nr and 0 <= next_c < nc:
                                    if board[next_r][next_c] == 'W':
                                        board[next_r][next_c] = 'x'
                                        stack.append((next_r, next_c))
                                    elif board[next_r][next_c] == '.' and not is_visited[next_r, next_c]:
                                        is_visited[next_r, next_c] = True
                                        n_empty_spaces += 1

                        if n_empty_spaces == 1:
                            ans = True
                            break

                if ans:
                    break

            ans = 'YES' if ans else 'NO'
            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
