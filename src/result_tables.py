from rich import print # type: ignore
from rich.table import Table # type: ignore
from src.casino import Casino
from src import users

def players_table(casino: Casino) -> None:
    '''
    Вывод таблицы rich о текущих игроках и их балансах. Также вывод инофрмации об активных ставках при наличии
    :param casino: Объект класса казино.
    :return: Ничего не возвращает
    '''
    player_table = Table(title="Players")
    player_table.add_column("Player", justify="center")
    player_table.add_column("Balance", justify="center")
    player_table.add_row("\n".join([player.name for player in casino.players.list]), "\n".join([str(player.balance.current_value()) for player in casino.players.list]))
    print(player_table)
    if casino.chips.bets_active():
        bets_table = Table(title="Remaining bets")
        bets_table.add_column("Player", justify="center")
        bets_table.add_column("Bet amount", justify="center", style="magenta")
        players: list[str] = []
        amounts: list[str] = []
        for plr in casino.chips.bets.keys():
            players.append(plr.name)
            amounts.append(str(plr.balance.current_value()))
        bets_table.add_row("\n".join(players), "\n".join(amounts))
        print(bets_table)



def gooses_table(casino: Casino) -> None:
    '''
    Вывод таблицы о гусях.
    :param casino: Объект класса казино.
    :return: Ничего не возвращает
    '''
    table = Table(title="Gooses")
    table.add_column("Regular goose")
    table.add_column("War goose")
    table.add_column("Honk goose, volume", justify="center")
    reg_gooses: list[str] = []
    war_gooses: list[str] = []
    honk_gooses: list[str] = []
    for goose in casino.gooses.list:
        match type(goose):
            case users.Goose:
                reg_gooses.append(goose.name)
            case users.WarGoose:
                war_gooses.append(goose.name)
            case users.HonkGoose:
                honk_gooses.append(f"{goose.name}, {goose.honk_volume}")
    table.add_row("\n".join(reg_gooses), "\n".join(war_gooses), "\n".join(honk_gooses))
    print(table)
