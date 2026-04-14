"""Player class"""


class Player:
    """Player class."""

    def __init__(self, name: str):
        self.__name = name
        self.__games = []


    def get_played_game_count(self) -> int:
        """Return the amount of games played."""
        return len(self.__games)

    def get_favourite_game_name(self) -> str:
        """Return the name of the most played game."""
        pass

    def get_won_game_count(self) -> int:
        """Return the number of games won."""
        pass

    def get_name(self):
        """Return name of player."""
        return self.__name