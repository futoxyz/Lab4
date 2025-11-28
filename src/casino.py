class CasinoBalance:
    def __init__(self, balance=0) -> None:
        self.balance: int = balance

    def __setitem__(self, value: int) -> None:
        if self.balance + value < 0:
            self.balance = 0
            return
        elif not self.balance:
            print("Player had no money to lose")
            return
        else:
            self.balance += value

class Chip:
    def __init__(self, amount=0):
        self.amount = amount
