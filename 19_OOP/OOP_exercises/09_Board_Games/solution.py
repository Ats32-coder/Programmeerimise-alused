"""
Board games statistics API.

This module parses board game results from a file and provides
query-based statistical access to players and games.
"""


class Player:
    """Represent a player and store their game statistics."""

    def __init__(self, name):
        """Initialize a player with a name."""
        self.name = name
        self.games_played = 0
        self.wins = 0
        self.game_count = {}

    def add_game(self, game_name):
        """Record a played game for the player."""
        self.games_played += 1
        self.game_count[game_name] = self.game_count.get(game_name, 0) + 1

    def add_win(self):
        """Increment the player's win counter."""
        self.wins += 1

    def favourite(self):
        """Return the most frequently played game."""
        return max(self.game_count, key=self.game_count.get)

    def handle(self, action):
        """Handle player statistic queries."""
        if action == "amount":
            return self.games_played
        if action == "won":
            return self.wins
        if action == "favourite":
            return self.favourite()


class Game:
    """Represent a board game and store all played rounds."""

    def __init__(self, name):
        """Initialize a game with a name."""
        self.name = name
        self.rounds = []
        self.wins = {}
        self.losses = {}
        self.player_games = {}
        self.player_counts = {}
        self.best_score = None
        self.record_holder = None

    def add_round(self, players, result_type, result):
        """Add a played round and update statistics."""
        self.rounds.append((players, result_type, result))

        count = len(players)
        self.player_counts[count] = self.player_counts.get(count, 0) + 1

        for p in players:
            self.player_games[p] = self.player_games.get(p, 0) + 1

        winner = self.get_winner(players, result_type, result)
        self.wins[winner] = self.wins.get(winner, 0) + 1

        loser = self.get_loser(players, result_type, result)
        if loser:
            self.losses[loser] = self.losses.get(loser, 0) + 1

        if result_type == "points":
            scores = list(map(int, result.split(",")))
            max_score = max(scores)
            if self.best_score is None or max_score > self.best_score:
                self.best_score = max_score
                self.record_holder = players[scores.index(max_score)]

    def get_winner(self, players, result_type, result):
        """Return winner of a round."""
        if result_type == "winner":
            return result

        if result_type == "places":
            return result.split(",")[0]

        scores = list(map(int, result.split(",")))
        return players[scores.index(max(scores))]

    def get_loser(self, players, result_type, result):
        """Return loser of a round."""
        if result_type == "winner":
            return None

        if result_type == "places":
            return result.split(",")[-1]

        scores = list(map(int, result.split(",")))
        return players[scores.index(min(scores))]

    def most_frequent_winner(self):
        """Return player with highest win ratio."""
        best_player = None
        best_ratio = -1

        for p in self.player_games:
            ratio = self.wins.get(p, 0) / self.player_games[p]
            if ratio > best_ratio:
                best_ratio = ratio
                best_player = p

        return best_player

    def most_frequent_loser(self):
        """Return player with highest loss ratio."""
        best_player = None
        best_ratio = -1

        for p in self.player_games:
            ratio = self.losses.get(p, 0) / self.player_games[p]
            if ratio > best_ratio:
                best_ratio = ratio
                best_player = p

        return best_player

    def handle(self, action):
        """Handle game statistic queries."""
        if action == "amount":
            return len(self.rounds)

        if action == "player-amount":
            return max(self.player_counts, key=self.player_counts.get)

        if action == "most-wins":
            return max(self.wins, key=self.wins.get)

        if action == "most-frequent-winner":
            return self.most_frequent_winner()

        if action == "most-losses":
            return max(self.losses, key=self.losses.get)

        if action == "most-frequent-loser":
            return self.most_frequent_loser()

        if action == "record-holder":
            return self.record_holder


class Statistics:
    """Provide statistics based on board game results file."""

    def __init__(self, filename):
        """Load statistics from file."""
        self.games = {}
        self.players = {}
        self.total_games = 0
        self.result_type_count = {"points": 0, "places": 0, "winner": 0}

        with open(filename) as f:
            for line in f:
                self._process_line(line.strip())

    def _process_line(self, line):
        """Process a single input line."""
        game_name, players_str, result_type, result = line.split(";")
        players = players_str.split(",")

        self.total_games += 1
        self.result_type_count[result_type] += 1

        if game_name not in self.games:
            self.games[game_name] = Game(game_name)

        game = self.games[game_name]

        for p in players:
            if p not in self.players:
                self.players[p] = Player(p)

        game.add_round(players, result_type, result)

        for p in players:
            self.players[p].add_game(game_name)

        winner = game.get_winner(players, result_type, result)
        self.players[winner].add_win()

    def get(self, path: str):
        """Return requested statistic based on path."""
        parts = path.strip("/").split("/")

        if parts[0] == "players":
            return list(self.players.keys())

        if parts[0] == "games":
            return list(self.games.keys())

        if parts[0] == "total":
            if len(parts) == 1:
                return self.total_games
            return self.result_type_count[parts[1]]

        if parts[0] == "player":
            return self.players[parts[1]].handle(parts[2])

        if parts[0] == "game":
            return self.games[parts[1]].handle(parts[2])