import random


class CodeBreaker:
    """Core logic for the 3-digit code guessing game."""

    def __init__(self):
        """Initialize game with a unique 3-digit secret code."""
        self.code = random.sample(range(10), 3)
        self.attempts = 10

    def guess(self, player_input):
        """Check guess and return (hits, misses)."""
        self.attempts -= 1

        nums = []
        for d in player_input:
            nums.append(int(d))

        hits = 0
        for i in range(3):
            if nums[i] == self.code[i]:
                hits += 1

        misses = 0
        for n in nums:
            if n in self.code:
                misses += 1

        misses = misses - hits

        return hits, misses


def main():
    """Main game loop for the user."""
    game = CodeBreaker()
    print("<<< KOODIMURDJA (3 unikaalset numbrit) >>>")

    while game.attempts > 0:
        inp = input(f"\n{game.attempts} katset jäänud. Arva: ")
        if len(inp) != 3 or not inp.isdigit():
            continue

        hits, misses = game.guess(inp)
        if hits == 3:
            print("VÕITSID!")
            return
        print(f"Tabamusi: {hits} | Pooltabamusi: {misses}")

    print(f"KAOTASID! Kood oli {game.code}")


if __name__ == "__main__":
    main()
