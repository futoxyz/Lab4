from src.constants import LOGO, STEP_LIST
from src.simulation import run_sim_steps
from time import sleep


def main() -> None:
    """
    Запуск программы. Принимает число шагов симуляции.
    :return: Ничего не возвращает.
    """
    print(LOGO)
    sleep(.5)
    print(STEP_LIST)
    try:
        steps = int(input("How many steps do you want to run in a simulation? > "))
    except ValueError as e:
        raise ValueError(e)

    try:
        seed = int(input("Enter seed for generation (optional) > "))
    except ValueError:
        seed = None
    run_sim_steps(steps, seed)


if __name__ == "__main__":
    main()
