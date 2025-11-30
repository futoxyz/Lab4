from src import users


class Casino:
    def __init__(self) -> None:
        self.players: users.PlayerCollection = users.PlayerCollection()
        self.gooses: users.GooseCollection = users.GooseCollection()

    def add_user(self, user: users.Player | users.Goose | users.WarGoose | users.HonkGoose) -> None:
        if type(user) is users.Player:
            self.players.__add__(user)
        elif isinstance(user, (users.Goose | users.WarGoose | users.HonkGoose)):
            self.gooses.__add__(user)
        else:
            raise TypeError(f"{user} isn't a player nor goose")

    def show_players(self) -> str:
        return self.players.show()

    def show_gooses(self) -> str:
        return self.gooses.show()
