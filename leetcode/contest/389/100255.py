class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        import bisect

        counter = Counter(word)

        freq = sorted(counter.values())
        n_freq = len(freq)
        prefix_sum = [0] * (n_freq + 1)
        prefix_sum[0] = freq[0]
        for i in range(1, n_freq):
            prefix_sum[i] = prefix_sum[i - 1] + freq[i]

        min_deletion = 10 ** 5 + 1
        for i in range(n_freq):
            cost = 0

            p = bisect.bisect_left(freq, freq[i])
            if p != 0:
                cost += prefix_sum[p - 1]

            j = bisect.bisect_right(freq, freq[i] + k)
            if j != n_freq:
                sum_j_to_n = prefix_sum[n_freq - 1] - prefix_sum[j - 1]
                cost += sum_j_to_n - (n_freq - j) * (freq[i] + k)

            min_deletion = min(min_deletion, cost)

        return min_deletion
