"""Board game statistics class"""
from player import Player
from game import Game
from play_session import PlaySession


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        self.__players : list[Player] = []
        self.__games : list[Game] = []
        self.__play_sessions : list[PlaySession]= []

    def get(self, path: str):
        """
        REST style path to invoke an action.
        "/game/{name}/amount"                   - tagastab int-i, mis kirjeldab, mitu mängu nimega name on mängitud
        "/game/{name}/player-amount"            - tagastab int-i, mis kirjeldab, mitme mängijaga mängu nimega game_name enim / kõige tihedamini mängitud on
        "/game/{name}/most-wins"                - tagastab mängija string, kellel on mängus nimega game_name enim võite (seda funktsiooni võidakse kutsuda ükskõik, mis tüüpi mängu korral)
        "/game/{name}/most-frequent-winner"     - tagastab mängija string, kelle võiduprotsent mängus nimega game_name on suurim (seda funktsiooni võidakse kutsuda ükskõik, mis tüüpi mängu korral)
        "/game/{name}/most-losses"              - tagastab mängija string, kellel on mängus nimega game_name enim kaotusi (viimasele kohale jäämisi) (seda funktsiooni kutsutakse vaid points või places mängu korral)
        "/game/{name}/most-frequent-loser"      - tagastab mängija string, kelle kaotuse protsent (protsent kordadest, kui mängija jäi viimasele kohale) mängus nimega game_name on suurim (seda funktsiooni kutsutakse vaid points või places mängu korral)
        "/game/{name}/record-holder"            - tagastab mängija (string), kes on mängus nimega game_name saanud enim punkte (ühe mängu jooksul), viigi korral tagastada see, kes selle tulemuse esimesena saavutas (seda funktsiooni kutsutakse vaid points mängu korral)
        """

        if path == "/players":
            return list(map(lambda p: p.get_name(), self.__players))
        elif path == "/games":
            return list(map(lambda p: p.get_name(), self.__games))
        return None
