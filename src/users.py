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
        self.dict: dict[str, Player] = {}

    def __add__(self, player: Player) -> None | str:
        if type(player) is not Player:
            raise IndexError(f"{player} is not a player!")
        elif player.name not in self.dict:
            self.dict[player.name] = player
            return None
        else:
            return f"{player.name} already added"

    def remove(self, player: Player) -> None | str:
        if type(player) is not Player:
            raise IndexError(f"{player} is not a player!")
        elif not self.dict[player.name]:
            return f"{player.name} is not in collection"
        else:
            self.dict.pop(player.name)
            return None

    def show(self) -> str:
        if not self.dict:
            return "Currently no players"
        return "\n".join([b.about() for a, b in self.dict.items()])


class GooseCollection:
    def __init__(self) -> None:
        self.dict: dict[str, Goose | WarGoose | HonkGoose] = {}

    def __add__(self, goose: Goose | WarGoose | HonkGoose):

        if goose.name not in self.dict:
            self.dict[goose.name] = goose
            return None
        else:
            return f"{goose.name} already added"

    def remove(self, goose: Goose | WarGoose | HonkGoose) -> None | str:

        if not self.dict[goose.name]:
            return f"{goose.name} is not in collection"
        else:
            self.dict.pop(goose.name)
            return None

    def show(self) -> str:
        if not self.dict:
            return "Currently no gooses"
        return "\n".join([b.about() for a, b in self.dict.items()])
