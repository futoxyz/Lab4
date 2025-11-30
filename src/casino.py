from src.users import Player, PlayerCollection, Goose, GooseCollection, WarGoose, HonkGoose


class Casino:
    def __init__(self) -> None:
        self.players: PlayerCollection = PlayerCollection()
        self.gooses: GooseCollection = GooseCollection()

    def add_user(self, user: Player | Goose | WarGoose | HonkGoose) -> None:
        if type(user) is Player:
            self.players.__add__(user)
        elif isinstance(user, (Goose | WarGoose | HonkGoose)):
            self.gooses.__add__(user)
        else:
            raise TypeError(f"{user} isn't a player nor goose")

    def show_players(self) -> str:
        return self.players.show()

    def show_gooses(self) -> str:
        return self.gooses.show()
