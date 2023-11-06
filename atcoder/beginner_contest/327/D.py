from collections import defaultdict, deque


def is_good_pair(a, b):
    adj = defaultdict(list)
    all_nodes = set()
    for a_i, b_i in zip(a, b):
        adj[a_i].append(b_i)
        adj[b_i].append(a_i)
        all_nodes.add(a_i)
        all_nodes.add(b_i)

    is_not_visited = all_nodes.copy()
    is_visited = defaultdict(bool)
    x = defaultdict(int)
    q = deque()
    while len(q) > 0 or len(is_not_visited) > 0:
        if len(q) == 0:
            u = is_not_visited.pop()
            is_visited[u] = True
            x[u] = 0
        else:
            u = q.popleft()

        for v in adj[u]:
            if is_visited[v]:
                if x[v] == x[u]:
                    return False
                else:
                    continue

            is_not_visited.remove(v)
            is_visited[v] = True
            x[v] = 1 - x[u]
            q.append(v)

    return True


def main():
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_eq_b = False
    for a_i, b_i in zip(a, b):
        if a_i == b_i:
            a_eq_b = True
            break

    ans = 'Yes' if not a_eq_b and is_good_pair(a, b) else 'No'
    print(ans)


if __name__ == '__main__':
    main()
