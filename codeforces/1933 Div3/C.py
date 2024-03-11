from math import gcd


def main():
    t = int(input())
    for _ in range(t):
        a, b, l = map(int, input().split())

        max_x = 0
        l_ = l
        while l_ % a == 0:
            l_ //= a
            max_x += 1

        max_y = 0
        l_ = l
        while l_ % b == 0:
            l_ //= b
            max_y += 1

        k = set()
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                z = pow(a, x) * pow(b, y)
                if z > l:
                    break

                if l % z == 0:
                    k.add(l // z)

        print(len(k))


if __name__ == '__main__':
    main()
