from collections import Counter

s = input()
counter = Counter(s)
most_freq = counter.most_common()[0][1]
most_freq_chars = [char for char, freq in counter.most_common() if freq == most_freq]
most_freq_chars.sort()
print(most_freq_chars[0])
