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


class WarGoose(Goose):
    def attack(self, player: Player) -> None:
        player.balance.__setitem__(player.name, -50)
        return


class HonkGoose(Goose):
    def scream(self, player: Player) -> None:
        player.balance.__setitem__(player.name, int(-100 * self.honk_volume))
        return
