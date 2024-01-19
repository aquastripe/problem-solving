def main():
    s1, s2 = input()
    t1, t2 = input()
    d_s = abs(ord(s1) - ord(s2))
    d_s = min(5 - d_s, d_s)
    d_t = abs(ord(t1) - ord(t2))
    d_t = min(5 - d_t, d_t)
    ans = 'Yes' if d_s == d_t else 'No'
    print(ans)


if __name__ == '__main__':
    main()
