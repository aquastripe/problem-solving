def main():
    a_b = []
    c_d = []

    n, m = map(int, input().split())
    for _ in range(m):
        a_b.append(tuple(map(lambda x: int(x) - 1, input().split())))

    k = int(input())
    for _ in range(k):
        c_d.append(tuple(map(lambda x: int(x) - 1, input().split())))

    ans = 0
    for sel in range(1 << (k + 1)):
        n_balls = [0] * n
        for i in range(k):
            selected_dish = c_d[i][(sel >> i) & 1]
            n_balls[selected_dish] += 1

        n_satisfied = 0
        for a, b in a_b:
            n_satisfied += n_balls[a] >= 1 and n_balls[b] >= 1

        ans = max(ans, n_satisfied)

    print(ans)


if __name__ == '__main__':
    main()
