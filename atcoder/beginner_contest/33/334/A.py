def main():
    b, g = map(int, input().split())
    s = ['Bat', 'Glove']
    ans = s[b < g]
    print(ans)


if __name__ == '__main__':
    main()
