import heapq



def read_list_int():
    return list(map(int, input().split()))


def read_tuple_int():
    return tuple(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m = read_tuple_int()
    a = read_list_int()
    INT_MAX = 2 ** 63 - 1
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = read_tuple_int()
        u -= 1
        v -= 1

        adj[u].append((v, w + a[v]))
        adj[v].append((u, w + a[u]))

    dist = [INT_MAX] * n
    pq = [(a[0], 0)]
    dist[0] = a[0]
    while len(pq) > 0:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            d = dist[u] + w
            if dist[v] > d:
                dist[v] = d
                heapq.heappush(pq, (d, v))

    print(*dist[1:])


if __name__ == '__main__':
    main()
