"""
1
5
1 1 1 1 1
-1 -1 -1 -1 -1

"""


def solve(a, b, n):
    c = list(zip(a, b))
    c.sort(key=lambda x: (-x[0], x[1]))
    rating_a = 0
    rating_b = 0
    m = 0
    for i in range(n):
        a_i, b_i = c[i]
        if a_i == 1 or a_i == 0 and b_i == -1:
            rating_a += a_i
            m += 1
        else:
            rating_b += b_i

    # here, rating_a is the maximal rating of a

    max_rating = min(rating_a, rating_b)
    for i in range(n - 1, m - 1, -1):
        a_i, b_i = c[i]
        rating = min(rating_a + a_i, rating_b - b_i)
        if max_rating < rating:
            max_rating = rating
            rating_a += a_i
            rating_b -= b_i

    for i in range(m - 1, -1, -1):
        a_i, b_i = c[i]
        rating = min(rating_a - a_i, rating_b + b_i)
        if max_rating < rating:
            max_rating = rating
            rating_a -= a_i
            rating_b += b_i
    return max_rating


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ans = solve(a, b, n)
        print(ans)


if __name__ == '__main__':
    main()
