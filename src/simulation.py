from src.casino import Casino
from src.constants import INIT_USERS
from src.result_tables import players_table, gooses_table
from src import users
from time import sleep
from rich.console import Console
from rich.rule import Rule
import random



def run_sim_steps(n: int, seed: int | None) -> None:
    '''
    Запуск n шагов симуляции. Проверка на ранний конец симуляции.
    :param n: Число шагов.
    :param seed: Сид генерации.
    :return: Ничего не возвращает.
    '''
    goosino = Casino()
    console = Console()
    for user in INIT_USERS:
        goosino.add_user(user, False)
    console.print(Rule(style="white"))
    console.print("Before simulation\n", style="bold")
    players_table(goosino)
    gooses_table(goosino)
    console.print(Rule(style="white"))
    print("Steps:\n")
    if seed is not None:
        random.seed(seed)

    for i in range(n):
        sleep(0.01)
        sim_over = True
        for player in goosino.players.list:
            if player.balance.current_value() > 0:
                sim_over = False
                break
        if sim_over:
            console.print(Rule(style="white"))
            console.print("After simulation\n", style="bold")
            players_table(goosino)
            print("All players reached 0 balance. Gooses took over the simulation!")
            return

        step_rtd = random.randint(1, 6)
        while step_rtd == 2 and not goosino.show_bets():
            step_rtd = random.randint(1, 6)

        match step_rtd:
            case 1:  # Создание ставки
                rand_player = random.choice(goosino.players.list)
                while rand_player.balance.current_value() == 0:
                    rand_player = random.choice(goosino.players.list)
                amount = random.randint(1, rand_player.balance.current_value())
                goosino.place_bet(rand_player, amount)
            case 2:  # Разрешение ставки
                goosino.resolve_bet()
            case 3:  # Атака от гуся на игрока
                rand_wargoose = random.choice(goosino.gooses.list)
                while type(rand_wargoose) is not users.WarGoose:
                    rand_wargoose = random.choice(goosino.gooses.list)
                rand_player = random.choice(goosino.players.list)

                print(rand_wargoose.attack(rand_player))
            case 4:  # Крик от гуся на игрока
                rand_honkgoose = random.choice(goosino.gooses.list)
                while type(rand_honkgoose) is not users.HonkGoose:
                    rand_honkgoose = random.choice(goosino.gooses.list)
                rand_player = random.choice(goosino.players.list)

                print(rand_honkgoose.scream(rand_player))
            case 5:  # Попытка кражи у игрока от любого гуся
                rand_goose = random.choice(goosino.gooses.list)
                rand_player = random.choice(goosino.players.list)
                print(rand_goose.steal_attempt(rand_player))
            case 6:  # Игрок ставит весь свой баланс
                rand_player = random.choice(goosino.players.list)
                while rand_player.balance.current_value() == 0:
                    rand_player = random.choice(goosino.players.list)
                goosino.place_bet(rand_player, rand_player.balance.current_value())

    console.print(Rule(style="white"))
    console.print("After simulation\n", style="bold")
    players_table(goosino)
