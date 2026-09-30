class Board:
    SIZE = 6

    def __init__(self):
        self.ships = []
        self.shots = set()

    def place_ship(self, cells):
        self.ships.append(set(cells))

    def fire(self, pos):
        if pos in self.shots:
            return False
        self.shots.add(pos)
        return any(pos in ship for ship in self.ships)

    def all_sunk(self):
        return bool(self.ships) and all(ship <= self.shots for ship in self.ships)

    def ship_sunk(self, pos):
        for ship in self.ships:
            if pos in ship:
                return ship <= self.shots
        return False