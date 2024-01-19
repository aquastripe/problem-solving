# 10/21/2023

from heapq import heappop, heappush, heapify


class PriorityQueue:

    def __init__(self, items=None):
        self.items = items if items is not None else []
        heapify(self.items)

    def pop(self):
        return heappop(self.items)

    def push(self, item):
        heappush(self.items, item)

    def is_empty(self):
        return len(self.items) == 0


def main():
    n = int(input())
    t_dt = [tuple(map(int, input().split())) for _ in range(n)]

    # Select by greedy:
    # - if there is no item, select the first item to enter;
    # - if there are items, select the first item to leave.
    t_closed_intervals = list(map(lambda x: (x[0], x[0] + x[1]), t_dt))
    t_closed_intervals.sort()
    pq = PriorityQueue()
    ans = 0
    t_now = 0
    i = 0
    while i < n or not pq.is_empty():
        # adjust t_now
        if i < n and pq.is_empty():
            t_begin, t_end = t_closed_intervals[i]
            t_now = t_begin

        # collect items which can be printed
        while i < n:
            t_begin, t_end = t_closed_intervals[i]
            if t_begin <= t_now <= t_end:
                pq.push(t_end)
                i += 1
            else:
                break

        # select the first to leave
        if not pq.is_empty():
            t_end = pq.pop()
            if t_now <= t_end:
                ans += 1
                t_now += 1

    print(ans)


if __name__ == "__main__":
    main()
