def main():
    t = int(input())
    for _ in range(t):
        hh, mm = map(int, input().split(':'))
        if hh >= 12:
            if hh > 12:
                print(f'{hh % 12:02d}:', end='')
            else:
                print(f'{hh:02d}:', end='')
            print(f'{mm:02d} PM')
        else:
            if hh == 0:
                hh += 12

            print(f'{hh:02d}:{mm:02d} AM')


if __name__ == '__main__':
    main()
