from src.casino import Casino
from src.constants import INIT_USERS
import random


def run_sim_steps(n: int, seed: int | None):
    goosino = Casino()

    for user in INIT_USERS:
        goosino.add_user(user)

    if seed is not None:
        random.seed = seed
    for i in range(n):
        step_rtd = random.randint(1, 6)
        while step_rtd == 2 and not goosino.show_bets():
            step_rtd = random.randint(1, 6)

        match step_rtd:
            case 1:




