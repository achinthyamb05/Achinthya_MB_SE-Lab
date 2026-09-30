import random


class AI:
    def __init__(self, size=6):
        self.size = size
        self.tried = set()
        self.target_queue = []

    def choose(self):
        while self.target_queue:
            pos = self.target_queue.pop(0)
            if pos not in self.tried:
                self.tried.add(pos)
                return pos

        options = [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
            if (r, c) not in self.tried
        ]

        if not options:
            return None

        pos = random.choice(options)
        self.tried.add(pos)
        return pos

    def record_result(self, pos, hit):
        if not hit:
            return

        r, c = pos
        neighbors = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        for neighbor in neighbors:
            nr, nc = neighbor
            if (
                0 <= nr < self.size
                and 0 <= nc < self.size
                and neighbor not in self.tried
                and neighbor not in self.target_queue
            ):
                self.target_queue.append(neighbor)