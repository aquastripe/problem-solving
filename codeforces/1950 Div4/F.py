from collections import deque


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        n_edges = 2 * a + b
        n_nodes = a + b + c

        if n_edges != n_nodes - 1:
            print(-1)
        else:
            q = deque([0])
            height = 0
            while len(q) > 0:
                height = q.popleft()

                if a > 0:
                    q.append(height + 1)
                    q.append(height + 1)
                    a -= 1
                elif b > 0:
                    q.append(height + 1)
                    b -= 1

            print(height)


if __name__ == '__main__':
    main()
