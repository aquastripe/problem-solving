# 1, 1, 1 = 3
# 1, 1, 11 = 13
# 1, 11, 11 = 23
# 11, 11, 11 = 33
# 1, 1, 111 = 113

# 0, 0, 0
# 0, 0, 1
# 0, 1, 1
# 1, 1, 1
# 0, 0, 2
# 0, 1, 2
# 1, 1, 2
# 0, 2, 2
# 1, 2, 2
# 2, 2, 2
def to_repunit(n):
    return int('1' * n)


def sum_three_repunits(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            for k in range(j + 1):
                count += 1

                if count == n:
                    return to_repunit(i + 1) + to_repunit(j + 1) + to_repunit(k + 1)


def main():
    n = int(input())
    ans = sum_three_repunits(n)
    print(ans)


if __name__ == '__main__':
    main()
