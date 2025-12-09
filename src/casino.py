from src import users


class Casino:
    def __init__(self) -> None:
        self.players = users.PlayerCollection()
        self.gooses = users.GooseCollection()
        self.chips = users.ChipCollection()

    def add_user(self, user: users.Player | users.Goose | users.WarGoose | users.HonkGoose) -> None:
        if type(user) is users.Player:
            self.players.add(user)
        elif isinstance(user, (users.Goose | users.WarGoose | users.HonkGoose)):
            self.gooses.add(user)
        else:
            raise TypeError(f"{user} isn't a player or goose")

    def show_players(self) -> str:
        return self.players.show()

    def show_gooses(self) -> str:
        return self.gooses.show()

    def show_bets(self) -> list[tuple[str, int]]:
        return self.chips.bets_active()

    def place_bet(self, player: users.Player, amount: int) -> None:
        if type(amount) is not int or type(player) is not users.Player:
            raise TypeError("Wrong type")
        if amount > player.balance.current_value():
            raise ValueError(f"{player.name} doesn't have enough balance!")
        self.chips.place_bet(player, amount)

    def resolve_bet(self) -> str:
        if not self.chips:
            return "Currently no bets"
        return self.chips.resolve_bet()
