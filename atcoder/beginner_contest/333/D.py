from collections import defaultdict


def dfs(graph, u, is_visited):
    count = 1
    stack = [u]
    is_visited[u] = True
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if is_visited[v]:
                continue

            is_visited[v] = True
            stack.append(v)
            count += 1
    return count


def main():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_visited = [False] * (n + 1)
    is_visited[1] = True
    n_child_nodes = []
    for v in graph[1]:
        n_child_nodes.append(dfs(graph, v, is_visited))

    ans = n - max(n_child_nodes)

    print(ans)


if __name__ == '__main__':
    main()
