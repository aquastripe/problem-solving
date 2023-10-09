import argparse
import itertools
from collections import defaultdict


def exponent_partitions(exponents, min_exponents):
    """Generate all vector partitions of 'exponents', each of whose
    entries is lexicographically at least 'min_exponents'."""
    if all(exponent == 0 for exponent in exponents):
        yield []
    else:
        for vector in itertools.product(*(range(v + 1) for v in exponents)):
            if vector >= min_exponents:
                remainder = tuple(x - y for x, y in zip(exponents, vector))
                for partition in exponent_partitions(remainder, vector):
                    yield partition + [vector]


def divisor_from_exponents(primes, exponent_vector):
    """Reconstruct divisor from the list of exponents."""
    divisor = 1
    for p, e in zip(primes, exponent_vector):
        divisor *= p ** e
    return divisor


def multiplicative_partitions(primes, exponents):
    """Generate all multiplication partitions of
    product(p**e for p, e in zip(primes, exponents))"""
    if len(exponents) == 0:
        # Corner case for partitions of 1.
        yield []
    else:
        initial_vector = (0,) * (len(exponents) - 1) + (1,)
        for partition in exponent_partitions(exponents, initial_vector):
            yield [divisor_from_exponents(primes, vector) for vector in partition]


def sum_41(prime_factors):
    primes = []
    exponents = []
    for prime, count in prime_factors.items():
        primes.append(prime)
        exponents.append(count)

    for factor_combination in multiplicative_partitions(primes, exponents):
        if sum(factor_combination) <= 41:
            return [1] * (41 - sum(factor_combination)) + factor_combination

    return -1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args()

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    with open(args.input_file, 'r', encoding='utf-8') as f_in, open(args.output_file, 'w', encoding='utf-8') as f_out:
        n_cases = int(f_in.readline())
        for case in range(n_cases):
            p = int(f_in.readline())
            n = p

            prime_factors = defaultdict(int)
            for prime in primes:
                while n % prime == 0:
                    prime_factors[prime] += 1
                    n //= prime

                if n < prime:
                    break

            if n != 1:
                ans = -1
            else:
                result = sum_41(prime_factors)
                if result == -1:
                    ans = -1
                else:
                    result.sort()
                    ans = f'{len(result)} ' + f' '.join(map(str, result))

            print(f'Case #{case + 1}: {ans}', file=f_out)


if __name__ == '__main__':
    main()
