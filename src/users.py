from random import randint
from src.money import CasinoBalance


class Player:
    def __init__(self, name: str, balance: int = 100) -> None:
        self.name = name
        self.balance: CasinoBalance = CasinoBalance(balance)

    def about(self) -> str:
        return f"{self.name}: {self.balance.current_value()}"


class Goose:
    def __init__(self, name: str, honk_volume=0.1) -> None:
        self.name = name
        self.honk_volume: float = honk_volume

    def about(self) -> str:
        return f"{self.name}: {self.honk_volume}"

    def steal_attempt(self, player: Player):
        dice = randint(0, 5) * 10
        amount = player.balance.current_value()
        if amount > dice:
            amount = dice
        player.balance.__setitem__(player.name, -amount)
        return f"{self.name} has stolen {amount} from {player.name}"


class WarGoose(Goose):
    def attack(self, player: Player) -> None:
        player.balance.__setitem__(player.name, -50)
        return


class HonkGoose(Goose):
    def scream(self, player: Player) -> None:
        player.balance.__setitem__(player.name, int(-100 * self.honk_volume))
        return


class PlayerCollection:
    def __init__(self) -> None:
        self.list: list[Player] = []

    def add(self, player: Player) -> None | str:
        if type(player) is not Player:
            raise IndexError(f"{player} is not a player!")
        elif player not in self.list:
            self.list.append(player)
            return None
        else:
            return f"{player.name} is already added"

    def remove(self, player: Player) -> None | str:
        if type(player) is not Player:
            raise IndexError(f"{player} is not a player!")
        elif player not in self.list:
            return f"{player.name} is not in collection"
        else:
            self.list.remove(player)
            return None

    def show(self) -> str:
        if not self.list:
            return "Currently no players"
        return "\n".join([player.about() for player in self.list])

    def __index__(self, key: int):
        if type(key) is not int:
            raise IndexError(f"{key} is not a number")
        if len(self.list) < key - 1 or key < 0:
            return f"No {key} in collection"
        else:
            return self.list[key].about()

    def __getitem__(self, item: int | slice) -> Player | list[Player]:
        try:
            return self.list[item]
        except IndexError as e:
            return e

    def __iter__(self):
        return iter(self.list)


class GooseCollection:
    def __init__(self) -> None:
        self.list: list[Goose | WarGoose | HonkGoose] = []

    def __add__(self, goose: Goose | WarGoose | HonkGoose):

        if goose not in self.list:
            self.list.append(goose)
            return None
        else:
            return f"{goose.name} already added"

    def remove(self, goose: Goose | WarGoose | HonkGoose) -> None | str:

        if not self.list[goose]:
            return f"{goose.name} is not in collection"
        else:
            self.list.remove(goose)
            return None

    def show(self) -> str:
        if not self.list:
            return "Currently no gooses"
        return "\n".join([goose.about() for goose in self.list])

    def __index__(self, key: int):
        if type(key) is not int:
            raise IndexError(f"{key} is not a number")
        if len(self.list) < key - 1 or key < 0:
            return f"No {key} in collection"
        else:
            return self.list[key].about()

    def __getitem__(self, item: int | slice) -> Goose | WarGoose | HonkGoose | list[Goose | WarGoose | HonkGoose]:
        try:
            return self.list[item]
        except IndexError as e:
            return e

    def __iter__(self):
        return iter(self.list)
