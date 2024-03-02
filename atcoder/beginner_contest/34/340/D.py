import heapq

from collections import defaultdict


def main():
    n = int(input())
    a, b, x = [0], [0], [0]
    for _ in range(n - 1):
        a_i, b_i, x_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        x.append(x_i)

    w = defaultdict(dict)
    for i in range(1, n):
        w[i][i + 1] = a[i] if i + 1 not in w[i] else min(w[i][i + 1], a[i])
        w[i][x[i]] = b[i] if x[i] not in w[i] else min(w[i][x[i]], b[i])

    pq = [(0, 1)]
    dist = [10 ** 16] * (n + 1)
    dist[1] = 0
    while len(pq) > 0:
        d, i = heapq.heappop(pq)
        if d > dist[i]:
            continue

        for j, d in w[i].items():
            if dist[j] > dist[i] + d:
                dist[j] = dist[i] + d
                heapq.heappush(pq, (dist[j], j))

    print(dist[n])


if __name__ == '__main__':
    main()
