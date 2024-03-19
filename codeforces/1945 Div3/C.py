def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input()
        zeros_left = [0] * (n + 1)
        ones_right = [0] * (n + 1)
        for i in range(n):
            zeros_left[i + 1] = zeros_left[i] + int(int(a[i]) == 0)
            ones_right[n - i - 1] = ones_right[n - i] + int(int(a[n - i - 1]) == 1)

        ans = 0
        min_dist = 10 ** 6
        for i in range(n + 1):
            n_zeros = zeros_left[i]
            n_ones = ones_right[i]

            if n_zeros >= ((i + 1) // 2) and n_ones >= ((n - i + 1) // 2):
                dist = abs(n - 2 * i)
                if dist < min_dist:
                    min_dist = dist
                    ans = i

        print(ans)


if __name__ == '__main__':
    main()
