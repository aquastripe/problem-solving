import bisect


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        """
        2 2 8
        i = 1
        mid = 2
        bisect_right = 2
        bisect_right - i = 1 #
        
        1 3 3 7
        i = 1
        mid = 3
        bisect_right = 3
        bisect_right - i = 2
        
        4 5 5 5 5
        i = 2
        bisect_right = 5
        bisect_right - i = 3
        
        1 1 2 2 3 4
        i = 2
        mid = 2
        bisect_right = 4
        bisect_right - i = 2
        
        1 2
        i = 0
        mid = 1
        bisect_right = 1
        bisect_right - i = 1
        """

        a.sort()
        i = n // 2 if n % 2 == 1 else n // 2 - 1
        mid = a[i]
        print(bisect.bisect_right(a, mid) - i)


if __name__ == '__main__':
    main()
