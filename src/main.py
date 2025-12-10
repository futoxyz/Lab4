from src.constants import LOGO
from src.casino import Casino

def main() -> None:
    """
    Создает казино, запускает генерацию событий, выводит все результаты.
    :return: Ничего не возвращает.
    """
    print(LOGO)

    goosino = Casino()
    goosino.show_players()

if __name__ == "__main__":
    main()
