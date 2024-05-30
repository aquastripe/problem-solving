def solve(s):
    in_letter = False
    last_digit = '0'
    last_letter = 'a'
    for s_i in s:
        if s_i.isdigit():
            if in_letter:
                return 'NO'

            if last_digit > s_i:
                return 'NO'

            last_digit = s_i
            in_letter = False
        else:
            if last_letter > s_i:
                return 'NO'

            last_letter = s_i
            in_letter = True
    return 'YES'


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ans = solve(s)
        print(ans)


if __name__ == '__main__':
    main()
