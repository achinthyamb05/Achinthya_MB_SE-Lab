from board import Board
from ai import AI


class Battleship:
    def __init__(self):
        self.player = Board()
        self.enemy = Board()
        self.ai = AI()
        self._setup()

    def _setup(self):
        # Player fleet
        self.player.place_ship({(1, 1), (1, 2), (1, 3)})
        self.player.place_ship({(4, 1), (4, 2)})

        # Enemy fleet
        self.enemy.place_ship({(2, 2), (2, 3), (2, 4)})
        self.enemy.place_ship({(4, 4), (4, 5)})

    def show(self):
        print("\nYour shots are coordinates like 2,3.")

        remaining = sum(
            len(ship - self.enemy.shots)
            for ship in self.enemy.ships
        )

        print("Ship cells remaining:", remaining)

    def run(self):
        print("Battleship")

        while True:
            self.show()

            raw = input("> ").strip().lower()

            if raw == "q":
                return

            try:
                r, c = map(int, raw.split(","))
                pos = (r - 1, c - 1)
            except ValueError:
                print("Use row,col.")
                continue

            if not (0 <= pos[0] < Board.SIZE and
                    0 <= pos[1] < Board.SIZE):
                print("Outside board.")
                continue

            if pos in self.enemy.shots:
                print("Already fired there.")
                continue

            # Player fires at enemy
            hit = self.enemy.fire(pos)

            if hit:
                print("HIT!")

                if self.enemy.ship_sunk(pos):
                    print("You sank a ship.")
            else:
                print("MISS!")

            if self.enemy.all_sunk():
                print("You sank the fleet.")
                return

            # AI fires at player
            ai_pos = self.ai.choose()

            if ai_pos is None:
                print("AI has no remaining moves.")
                return

            ar, ac = ai_pos
            print("AI fired at", f"{ar + 1},{ac + 1}")

            if any(ai_pos in ship for ship in self.player.ships):
                print("AI scored a hit")
                self.player.shots.add(ai_pos)
                self.ai.record_result(ai_pos, True)

                if self.player.ship_sunk(ai_pos):
                    print("AI sank your ship.")
            else:
                print("AI missed")
                self.player.shots.add(ai_pos)
                self.ai.record_result(ai_pos, False)