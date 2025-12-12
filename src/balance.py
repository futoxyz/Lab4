import logging
from datetime import datetime
logger = logging.getLogger(__name__)


def current_time() -> str:
    '''
    :return: Текущее время в формате для логгирования.
    '''
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class CasinoBalance:
    def __init__(self, balance=0) -> None:
        '''
        :param balance: Баланс, изменения которого всегда логгируются.
        '''
        self.balance: int = balance

    def __setitem__(self, key, value: int) -> None:
        '''
        Изменение баланса. Проверяет, можно ли списать заданное значение и не уйти в минус.
        Невозможно сделать ставку больше, чем баланс, поэтому при ней уйти в минус нельзя.
        При атаке/крике/краже от гуся если пытается списать больше, чем есть, то списывается до 0.
        :param key: Имя игрока.
        :param value: Изменение баланса (с учётом знака).
        :return: Ничего не возвращает.
        '''
        logging.basicConfig(filename='balance.log', level=logging.INFO)

        if self.balance == 0 and value < 0:
            logger.info(f"[{current_time()}] {key} had 0 and could not lose any more")
        elif self.balance + value < 0:
            logger.info(f"[{current_time()}] {key} balance went from {self.balance} to {0}")
            self.balance = 0
        else:
            logger.info(f"[{current_time()}] {key} balance went from {self.balance} to {self.balance + value}")
            self.balance += value

    def current_value(self) -> int:
        '''
        :return: Баланс.
        '''
        return self.balance
