def main():
    n = input()
    s = input()
    pos = s.find('ABC')
    ans = pos + 1 if pos != -1 else pos
    print(ans)


if __name__ == '__main__':
    main()
