def main():
    s = input()
    if s[0] == '<' and s[-1] == '>' and all(s[i] == '=' for i in range(1, len(s) - 1)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
