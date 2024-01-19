def main():
    s = input()
    stack = []
    for i in range(len(s)):
        stack.append(s[i])

        while len(stack) >= 3 and stack[-3:] == ['A', 'B', 'C']:
            stack.pop()
            stack.pop()
            stack.pop()

    print(''.join(stack))


if __name__ == '__main__':
    main()
