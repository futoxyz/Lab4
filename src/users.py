import random
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

    def steal_attempt(self, player: Player) -> str:
        dice = random.randint(0, 5) * 10
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

    def __index__(self, key: int) -> str:
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
            raise IndexError(e)

    def __iter__(self):
        return iter(self.list)


class GooseCollection:
    def __init__(self) -> None:
        self.list: list[Goose | WarGoose | HonkGoose] = []

    def add(self, goose: Goose | WarGoose | HonkGoose):

        if goose not in self.list:
            self.list.append(goose)
            return None
        else:
            return f"{goose.name} already added"

    def remove(self, goose: Goose | WarGoose | HonkGoose) -> None | str:

        if goose not in self.list:
            return f"{goose.name} is not in collection"
        else:
            self.list.remove(goose)
            return None

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

    def __getitem__(self, item: int | slice) -> Goose | list[Goose | WarGoose | HonkGoose]:
        try:
            return self.list[item]
        except IndexError:
            raise IndexError("Bad input")

    def __iter__(self):
        return iter(self.list)


class ChipCollection:
    def __init__(self) -> None:
        self.bets: dict[Player, CasinoBalance] = {}

    def place_bet(self, player: Player, amount: int) -> str:
        if amount == player.balance.current_value():
            self.bets[player] = CasinoBalance(amount)
            return f"{player.name} went all-in!"
        self.bets[player] = CasinoBalance(amount)
        return f"{player.name} made a {amount} bet"

    def bets_active(self) -> list[tuple[str, int]]:
        return [(a.name, b.current_value()) for a,b in self.bets.items()]

    def resolve_bet(self) -> str:
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
