import math


def main():
    n_digits_s = int(input())
    s = int(''.join(sorted(list(input()), reverse=True)))

    max_square_root = int(math.sqrt(s))
    digit_freq_s = [0] * 10
    digit_freq_s[s % 10] += 1
    while (s := s // 10) > 0:
        digit_freq_s[s % 10] += 1

    n_square_numbers = 0
    for t_square_root in range(max_square_root + 1):
        t = t_square_root * t_square_root
        digit_freq_t = [0] * 10
        digit_freq_t[t % 10] += 1
        while (t := t // 10) > 0:
            digit_freq_t[t % 10] += 1

        n_digits_t = sum(digit_freq_t)
        digit_freq_t[0] += max(n_digits_s - n_digits_t, 0)
        if digit_freq_s == digit_freq_t:
            n_square_numbers += 1

    print(n_square_numbers)


if __name__ == '__main__':
    main()
