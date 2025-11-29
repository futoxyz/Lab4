from src.users import Player, Goose, WarGoose, HonkGoose


class Casino:
    def __init__(self) -> None:
        self.player_list: dict[str, Player] = {}
        self.goose_list: dict[str, Goose | WarGoose | HonkGoose] = {}

    def add_user(self, user: Player | Goose | WarGoose | HonkGoose) -> None:
        if type(user) is Player:
            self.player_list[user.name] = user
        elif type(user) is Goose | WarGoose | HonkGoose:
            self.goose_list[user.name] = user
        else:
            raise TypeError(f"{user} isn't a player nor goose")

    def show_players(self) -> str:
        if not self.player_list:
            return "Currently no players"
        return "\n".join([b.about() for a, b in self.player_list.items()])

    def show_gooses(self) -> str:
        if not self.goose_list:
            return "Currently no gooses"
        return "Gooses and their honk volumes\n" + "\n".join([b.about() for a, b in self.goose_list.items()])
