def main():
    n, m = tuple(map(int, input().split()))
    s = input()
    t = input()
    is_prefix = s == t[:n]
    is_suffix = s == t[-n:]
    if is_prefix and is_suffix:
        print(0)
    elif is_prefix:
        print(1)
    elif is_suffix:
        print(2)
    else:
        print(3)


if __name__ == '__main__':
    main()
