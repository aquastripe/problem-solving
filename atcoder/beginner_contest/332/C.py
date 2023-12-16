def main():
    n, m = map(int, input().split())
    s = input()
    max_count_logo, max_plain_and_logo = 0, 0

    count_plain, count_logo, count_plain_and_logo = 0, 0, 0
    for s_i in s:
        if s_i == '0':
            max_count_logo = max(max_count_logo, count_logo)
            max_plain_and_logo = max(max_plain_and_logo, count_plain + count_logo)
            count_plain, count_logo, count_plain_and_logo = 0, 0, 0
        elif s_i == '1':
            count_plain += 1
        else:
            count_logo += 1
    max_count_logo = max(max_count_logo, count_logo)
    max_plain_and_logo = max(max_plain_and_logo, count_plain + count_logo)

    ans = max_count_logo
    if max_count_logo + m < max_plain_and_logo:
        ans += max_plain_and_logo - (max_count_logo + m)

    print(ans)


if __name__ == '__main__':
    main()
