from collections import defaultdict


def main():
    n = int(input())
    s = input()
    count_all = defaultdict(int)
    count = 0
    prev_character = None
    for s_i in s:
        if s_i == prev_character:
            count += 1
        else:
            count = 1

        if count > count_all[s_i]:
            count_all[s_i] = count

        prev_character = s_i

    print(sum(count_all.values()))


if __name__ == '__main__':
    main()
