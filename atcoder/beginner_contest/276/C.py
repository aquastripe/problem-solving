def reverse_after(nums, i):
    nums[i:] = nums[::-1][:len(nums) - i]


def method_1(n, p):
    j = n - 1
    while j - 1 >= 0 and p[j - 1] < p[j]:
        j -= 1
    successor = j - 1
    if successor >= 0:
        reverse_after(p, successor + 1)

        i = successor + 1
        while p[i] > p[successor]:
            i += 1
        pivot = i

        p[pivot], p[successor] = p[successor], p[pivot]
        # pivot, successor = successor, pivot
    else:
        reverse_after(p, 0)


def main():
    n = int(input())
    p = list(map(int, input().split()))

    method_1(n, p)

    print(*p)


if __name__ == '__main__':
    main()
