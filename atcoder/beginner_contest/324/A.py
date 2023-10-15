def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 'Yes' if all(a[0] == a_i for a_i in a) else 'No'
    print(ans)


if __name__ == '__main__':
    main()
