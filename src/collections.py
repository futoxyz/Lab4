from src import users
from src.balance import CasinoBalance
import random


class PlayerCollection:
    def __init__(self) -> None:
        '''
        Коллекция игроков в виде списка.
        '''
        self.list: list[users.Player] = []

    def add(self, player: users.Player, inform: bool) -> None:
        '''
        :param player: Добавляемый игрок.
        :param inform: Условие вывода информации о добавлении.
        :return: Информация о добавлении.
        '''
        if type(player) is not users.Player:
            raise IndexError(f"{player} is not a player!")
        self.list.append(player)
        if inform:
            print(f"Player \"{player.name}\" was added")

    def remove(self, player: users.Player) -> str:
        '''
        :param player: Удаляемый игрок.
        :return: Информация об удалении/невозможности удаления.
        '''
        if type(player) is not users.Player:
            raise IndexError(f"{player} is not a player!")
        elif player not in self.list:
            return f"{player.name} is not in collection"
        else:
            self.list.remove(player)
            return f"Player \"{player.name}\" was removed"

    def show(self) -> str:
        '''
        :return: Вывод всех игроков в коллекции.
        '''
        if not self.list:
            return "Currently no players"
        return "\n".join([player.about() for player in self.list])

    def __index__(self, key: int) -> str:
        '''
        Метод индексирования.
        '''
        if type(key) is not int:
            raise IndexError(f"{key} is not a number")
        if len(self.list) < key - 1 or key < 0:
            return f"No {key} in collection"
        else:
            return self.list[key].about()

    def __getitem__(self, item: int | slice) -> users.Player | list[users.Player]:
        '''
        Метод среза.
        '''
        try:
            return self.list[item]
        except IndexError as e:
            raise IndexError(e)

    def __iter__(self):
        '''
        Метод итерации.
        '''
        return iter(self.list)


class GooseCollection:
    '''
    Коллекция, аналогичная коллекции игроков по функционалу.
    '''
    def __init__(self) -> None:
        self.list: list[users.Goose | users.WarGoose | users.HonkGoose] = []

    def add(self, goose: users.Goose | users.WarGoose | users.HonkGoose, inform: bool) -> None:
        if not isinstance(goose, users.Goose | users.WarGoose | users.HonkGoose):
            raise IndexError(f"{goose} is not a goose!")
        self.list.append(goose)
        if inform:
            print(f"Goose \"{goose.name}\" was added")

    def remove(self, goose: users.Goose | users.WarGoose | users.HonkGoose) -> None | str:

        if goose not in self.list:
            return f"{goose.name} is not in collection"
        else:
            self.list.remove(goose)
            return f"Goose \"{goose.name}\" was removed"

    def show(self) -> str:
        if not self.list:
            return "Currently no gooses"
        return "\n".join([goose.about() for goose in self.list])

    def __index__(self, key: int) -> str:
        if type(key) is not int:
            raise IndexError(f"{key} is not a number")
        if len(self.list) < key - 1 or key < 0:
            return f"No {key} in collection"
        else:
            return self.list[key].about()

    def __getitem__(self, item: int | slice) -> users.Goose | list[users.Goose | users.WarGoose | users.HonkGoose]:
        try:
            return self.list[item]
        except IndexError as e:
            raise IndexError(e)

    def __iter__(self):
        return iter(self.list)


class ChipCollection:
    def __init__(self) -> None:
        '''
        Коллекция всех ставок в казино. Хранит словарь с инофрмацией об игроке и его ставке.
        '''
        self.bets: dict[users.Player, CasinoBalance] = {}

    def place_bet(self, player: users.Player, amount: int) -> str:
        '''
        Создает ставку от игрока.
        :param player: Игрок.
        :param amount: Размер ставки.
        :return: Информация о создании ставки. Особое уведомление, если игрок идет all-in.
        '''
        if amount > player.balance.current_value():
            raise ValueError(f"{player.name} doesn\'t have enough balance!")
        if amount == 0:
            return "Cannot bet 0"

        if amount == player.balance.current_value():
            self.bets[player] = CasinoBalance(amount)
            return f"{player.name} went all-in!"
        self.bets[player] = CasinoBalance(amount)
        return f"{player.name} made a {amount} bet"

    def bets_active(self) -> list[tuple[str, int]]:
        '''
        :return: Вывод ставок.
        '''
        return [(a.name, b.current_value()) for a,b in self.bets.items()]

    def resolve_bet(self) -> str:
        '''
        Закрывает самую старую ставку (ставки закрываются в очереди).
        Случайно генерируется коэффициент ставки от 0.5 до 1.5, который определяет выигрыш и шанс на него.
        Самый высокий шанс - 75% при ставке 0.5, самый низкий - 25% при ставке 1.5.
        :return: Информация о победе/поражении.
        '''
        player, amount = next(iter(self.bets.items()))
        del self.bets[player]
        coef = round(random.random() + 0.5, 1)
        outcome = random.randint(1, 100)

        if outcome <= (2 - coef) * 50:
            winning = int(amount.current_value() * coef)
            player.balance.__setitem__(player.name, winning)
            return f"{player.name} won {winning} from his bet!"
        else:
            player.balance.__setitem__(player.name, -amount.current_value())
            return f"{player.name} lost {amount.current_value()} from his bet!"
