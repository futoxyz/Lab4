import logging
from datetime import datetime
logger = logging.getLogger(__name__)


def current_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class CasinoBalance:
    def __init__(self, balance=0) -> None:
        self.balance: int = balance

    def __setitem__(self, key, value: int) -> None:
        logging.basicConfig(filename='balance_updates.log', level=logging.INFO)

        if self.balance == 0 and value < 0:
            logger.info(f"[{current_time()}] {key} had 0 and could not lose any more")
            return
        elif self.balance + value < 0:
            logger.info(f"[{current_time()}] {key} balance went from {self.balance} to {0}")
            self.balance = 0
            return
        else:
            logger.info(f"[{current_time()}] {key} balance went from {self.balance} to {self.balance + value}")
            self.balance += value
            return

    def current_value(self) -> int:
        return self.balance


class Chip:
    def __init__(self, amount=0) -> None:
        self.amount = amount
