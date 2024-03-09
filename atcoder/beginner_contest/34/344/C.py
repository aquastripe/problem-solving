from itertools import product


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    l = int(input())
    c = list(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))

    ans_set = set()
    for a_i, b_i, c_i in product(a, b, c):
        ans_set.add(a_i + b_i + c_i)

    for x_i in x:
        if x_i in ans_set:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
