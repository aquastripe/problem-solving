from dataclasses import dataclass, field
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


class EventType:
    PERSON_RETURNS: int = 0
    NOODLE_IS_FLOWN_DOWN: int = 1


@dataclass(order=True)
class Event:
    t_i: int
    event_type: int
    p: int = field(compare=False)
    w_i: int = field(compare=False)
    s_i: int = field(compare=False)


def main():
    n, m = list(map(int, input().split()))
    event_queue = PriorityQueue()
    for _ in range(m):
        t_i, w_i, s_i = list(map(int, input().split()))
        event_queue.push(Event(t_i, EventType.NOODLE_IS_FLOWN_DOWN, -1, w_i, s_i))

    people_queue = PriorityQueue(list(range(n)))
    all_amount_of_noodles = [0] * n
    while not event_queue.is_empty():
        event = event_queue.pop()

        if event.event_type == EventType.PERSON_RETURNS:
            people_queue.push(event.p)
        else:
            if not people_queue.is_empty():
                p = people_queue.pop()
                event_queue.push(Event(event.t_i + event.s_i, EventType.PERSON_RETURNS, p, -1, -1))
                all_amount_of_noodles[p] += event.w_i

    for amount_of_noodles in all_amount_of_noodles:
        print(amount_of_noodles)


if __name__ == '__main__':
    main()
