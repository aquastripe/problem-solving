def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


"""
n m
4 3

000 & 011 = 0
001 & 011 = 1
010 & 011 = 1
011 & 011 = 2
100 & 011 = 0

1: 2
2: 1

n m
9 5

1 0001 & 0101 = 1
3 0011 & 0101 = 1

4 0100 & 0101 = 1
6 0110 & 0101 = 1
  1100
  1110

9 1001 & 0101 = 1
5 0101 & 0101 = 2
7 0111 & 0101 = 2


n m
9 25
1 0001 & 11001 = 1
3 0011 & 11001 = 1

5 0101 & 11001 = 1
7 0111 & 11001 = 1

8 1000 & 11001 = 1

9 1001 & 11001 = 2

2 0010 & 11001 = 0
4 0100 & 11001 = 0
6 0110 & 11001 = 0

1: X
0: Y
C(X, 1) * 2^Y + C(X, 2) * 2^Y
2 * 4 + 
"""


def main():
    n, m = read_tuple_int()
    max_bit_length = max(n.bit_length(), m.bit_length())
    count_1s = m.bit_count()
    count_0s = max_bit_length - count_1s

    for i in range(max_bit_length):
        for j in range(max_bit_length):
            ...


if __name__ == '__main__':
    main()
