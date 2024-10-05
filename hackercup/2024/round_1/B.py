import argparse
import bisect


def sieve(end):
    # prime[i] is going to store
    # true if if i*2 + 1 is composite.
    is_prime = [0 if i % 2 == 0 else 1 for i in range(end + 1)]
    is_prime[1] = 0
    is_prime[2] = 1
    # 2 is the only even prime so
    # we can ignore that. Loop
    # starts from 3.
    i = 3
    while i * i <= end:
        # If i is prime, mark all its
        # multiples as composite
        if is_prime[(i)] == 1:
            j = i * i
            while j <= end:
                is_prime[j] = 0
                j += 2 * i
        i += 2
    # writing 2 separately
    # Printing other primes
    i = 2
    primes = []
    while i <= end:
        if is_prime[i]:
            primes.append(i)
        i += 1
    return primes, is_prime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        primes, is_prime = sieve(10_000_010)
        for case in range(n_cases):
            n = int(f_in.readline())

            if n < 5:
                ans = 0
            else:
                ans = 2
                for p in primes[2:]:
                    if p + 2 <= n:
                        if is_prime[p + 2]:
                            ans += 1
                    else:
                        break

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
