def is_palindrome(s):
    for i in range(len(s) // 2 + 1):
        if s[i] != s[-i - 1]:
            return False

    return True


def main():
    s = input()
    longest_palindrome = 1
    longest_palindrome_is_found = False
    for i in range(len(s)):
        test_length = len(s) - i
        for j in range(i + 1):
            if is_palindrome(s[j:j + test_length]):
                longest_palindrome = test_length
                longest_palindrome_is_found = True
                break

        if longest_palindrome_is_found:
            break

    print(longest_palindrome)


if __name__ == '__main__':
    main()
