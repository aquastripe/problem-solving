from collections import defaultdict


def main():
    n, t = map(int, input().split())

    count_scores = defaultdict(int)
    count_scores[0] = n
    scores = defaultdict(int)
    for _ in range(t):
        a_i, b_i = map(int, input().split())
        a_i -= 1

        count_scores[scores[a_i]] -= 1
        if count_scores[scores[a_i]] == 0:
            count_scores.pop(scores[a_i])

        scores[a_i] += b_i
        count_scores[scores[a_i]] += 1
        print(len(count_scores))


if __name__ == '__main__':
    main()
