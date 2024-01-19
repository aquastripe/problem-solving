def main():
    n = int(input())
    a = set(map(int, input().split()))
    a_max = max(a)
    a.remove(a_max)
    print(max(a))


if __name__ == '__main__':
    main()
