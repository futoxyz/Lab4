from src.casino import CasinoBalance


class Player:
    def __init__(self, name: str):
        self.name = name
        self.balance: CasinoBalance = CasinoBalance()


class Goose:
    def __init__(self, name: str, honk_volume=0.5):
        self.name = name
        self.honk_volume: float = honk_volume


class WarGoose(Goose):
    def attack(self, player: Player):
        return

class HonkGoose(Goose):
    def scream(self, player: Player):
        return
