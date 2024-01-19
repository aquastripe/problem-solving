def main():
    x, y = list(map(int, input().split()))
    ans = 'Yes' if -3 <= y - x <= 2 else 'No'
    print(ans)


if __name__ == '__main__':
    main()
