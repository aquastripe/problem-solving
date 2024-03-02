from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))

    max_square_number = 2 * 10 ** 5
    square_numbers = []
    num = 1
    while (n_square := num * num) < max_square_number + 1:
        square_numbers.append(n_square)
        num += 1

    """
    Building a table like:
    0 -> 0
    1 -> 1
    2 -> 2
    3 -> 3
    4 -> 1
    """

    b = []
    for a_i in a:
        if a_i == 0:
            b.append(a_i)
            continue

        for j in range(len(square_numbers) - 1, -1, -1):
            if a_i % square_numbers[j] == 0:
                b.append(a_i // square_numbers[j])
                break

    count = Counter(b)
    """
    Case 1: 0 can be paired with non-0, 
            and the combination number is count[0] * count[non-0] = count[0] * (n - count[0]).
    Case 2: Two same numbers are paired, and the combination number is C(count[num], 2).
    """
    ans = count[0] * (n - count[0]) + sum(freq * (freq - 1) // 2 for freq in count.values())
    print(ans)


if __name__ == '__main__':
    main()
