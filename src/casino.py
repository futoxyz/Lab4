from src import users, collections

class Casino:
    '''
    Главное казино с коллекцией игроков, гусей и ставок.
    '''
    def __init__(self) -> None:
        self.players = collections.PlayerCollection()
        self.gooses = collections.GooseCollection()
        self.chips = collections.ChipCollection()

    def add_user(self, user: users.Player | users.Goose | users.WarGoose | users.HonkGoose) -> None:
        '''
        Добавляет игрока или гуся в казино. Функция сама определяет тип и добавляет пользователя в нужную коллекцию.
        :param user: Добавляемый пользователь.
        :return: Ничего не возвращает. Выводит информацию о добавлении.
        '''
        if type(user) is users.Player:
            print(self.players.add(user))
        elif isinstance(user, (users.Goose | users.WarGoose | users.HonkGoose)):
            print(self.gooses.add(user))
        else:
            raise TypeError(f"{user} isn't a player or goose")

    def show_players(self) -> str:
        return self.players.show()

    def show_gooses(self) -> str:
        return self.gooses.show()

    def show_bets(self) -> list[tuple[str, int]]:
        return self.chips.bets_active()

    def place_bet(self, player: users.Player, amount: int) -> None:
        '''
        Дополнительные проверки для ставки, включая проверку на наличие баланса для значения ставки.
        :return: Ничего не возвращает.
        '''
        if type(amount) is not int or type(player) is not users.Player:
            raise TypeError("Wrong type")
        if amount > player.balance.current_value():
            raise ValueError(f"{player.name} doesn't have enough balance!")
        print(self.chips.place_bet(player, amount))

    def resolve_bet(self) -> None:
        if not self.chips:
            print("Currently no bets")
        print(self.chips.resolve_bet())
