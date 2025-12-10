from src.constants import LOGO, STEP_LIST
from src.simulation import run_sim_steps
from time import sleep

def main() -> None:
    """
    Создает казино, запускает генерацию событий, выводит все результаты.
    :return: Ничего не возвращает.
    """
    print(LOGO)
    sleep(1)
    print(STEP_LIST)
    try:
        steps = int(input("How many steps do you want to run in a simulation? > "))
    except ValueError as e:
        raise ValueError(e)

    try:
        seed = int(input("Enter seed for generation (optional) > "))
    except:
        seed = None
    run_sim_steps(steps, seed)


if __name__ == "__main__":
    main()
