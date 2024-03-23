def solve(s, w, b):
    for i in range(14):
        count_w = 0
        count_b = 0
        j = 0
        while count_w < w:
            if s[i + j] == 'w':
                count_w += 1
            else:
                count_b += 1

            if count_w == w and count_b == b:
                return True

            j += 1

        count_w = 0
        count_b = 0
        j = 0
        while count_b < b:
            if s[i + j] == 'w':
                count_w += 1
            else:
                count_b += 1

            if count_w == w and count_b == b:
                return True

            j += 1

    return False


def main():
    w, b = map(int, input().split())
    s = 'wbwbwwbwbwbw'
    s = ''.join([s] * 100)
    ans = 'Yes' if solve(s, w, b) else 'No'
    print(ans)


if __name__ == '__main__':
    main()
