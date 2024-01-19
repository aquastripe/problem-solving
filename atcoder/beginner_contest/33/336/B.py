def main():
    n = int(input())
    count_zeros = 0
    while n & 1 == 0:
        count_zeros += 1
        n >>= 1

    print(count_zeros)


if __name__ == '__main__':
    main()
