def solve(x):
    min_dist = 1000
    for a in range(1, 11):
        dist = 0
        for x_i in x:
            dist += abs(a - x_i)

        if min_dist > dist:
            min_dist = dist

    return min_dist


def main():
    t = int(input())
    for _ in range(t):
        x = list(map(int, input().split()))
        ans = solve(x)
        print(ans)


if __name__ == '__main__':
    main()
