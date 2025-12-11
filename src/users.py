import random
from src.balance import CasinoBalance


class Player:
    def __init__(self, name: str, balance: int = 200) -> None:
        '''
        :param name: Имя игрока.
        :param balance: Баланс игрока в виде объекта из класса CasinoBalance.
        '''
        self.name = name
        self.balance: CasinoBalance = CasinoBalance(balance)

    def about(self) -> str:
        '''
        :return: Вывод иноформации об игроке.
        '''
        return f"{self.name}: {self.balance.current_value()}"


class Goose:
    def __init__(self, name: str, honk_volume=0.1) -> None:
        '''
        :param name: Имя гуся.
        :param honk_volume: Громкость крика (float от 0 до 1).
        '''
        self.name = name
        self.honk_volume: float = honk_volume

    def about(self) -> str:
        '''
        :return: Вывод иноформации о гусе.
        '''
        return f"{self.name}: {self.honk_volume}"

    def steal_attempt(self, player: Player) -> str:
        '''
        Попытка украть у игрока деньги. Может украсть от 10 до 50 валюты, но может и не украсть ничего.
        :param player: Игрок, у которого пытается украсть гусь.
        :return: Информация о попытке кражи.
        '''
        dice = random.randint(0, 5) * 10
        amount = player.balance.current_value()
        if amount > dice:
            amount = dice
        player.balance.__setitem__(player.name, -amount)
        return f"{self.name} has stolen {amount} from {player.name}"


class WarGoose(Goose):
    '''
    Подкласс гуся, который может атаковать игрока. Успешная атака отнимает 50 валюты (или меньше) у игрока.
    '''
    def attack(self, player: Player) -> str:
        player.balance.__setitem__(player.name, -50)
        return f"{self.name} attacked {player.name}! Player lost 50 balance"


class HonkGoose(Goose):
    '''
    Подкласс гуся, который может накричать на игрока. Баланс игрока изменяется в зависимости от громкости крика (до 100 валюты).
    '''
    def scream(self, player: Player) -> str:
        player.balance.__setitem__(player.name, int(-100 * self.honk_volume))
        return f"{self.name} screamed at {player.name}! Player lost {int(100 * self.honk_volume)} balance"
