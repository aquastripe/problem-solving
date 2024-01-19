# L <= A+KM <= R
# 1. A+KM >= L
#    -> K >= (L-A)/M
#    -> K = ceil((L-A)/M)
# 2. A+KM <= R
#    -> K <= (R-A)/M
#    -> K = floor((R-A)/M)
def ceil_div(a, b):
    """
    ceil(a/b) for integers
    """
    return a // b + (1 if a % b != 0 else 0)


def floor_div(a, b):
    """
    floor(a/b) for integers
    """
    return a // b


def main():
    a, m, l, r = map(int, input().split())
    k_l = ceil_div(l - a, m)
    k_r = floor_div(r - a, m)
    ans = k_r - k_l + 1
    print(ans)


if __name__ == '__main__':
    main()
