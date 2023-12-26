def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        mask = 0
        ans = a ^ mask + b ^ mask

        for i in range(10):
            test_bit = (1 << i)
            if test_bit > a and test_bit > b:
                break

            temp_mask = mask | test_bit
            temp_result = a ^ temp_mask + b ^ temp_mask
            if ans > temp_result:
                ans = temp_result
                mask = temp_mask

        print(ans)


if __name__ == '__main__':
    main()
