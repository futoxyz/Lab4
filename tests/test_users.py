import pytest
from src import users
from src.collections import ChipCollection


def test_player_bets() -> None:
    '''
    Тест ставок игрока.
    :return: Ничего не возвращает.
    '''
    ethan = users.Player("Ethan", 200)
    chip_col = ChipCollection()

    chip_col.place_bet(ethan, 50)

    assert chip_col.bets_active() == [('Ethan', 50)]
    chip_col.resolve_bet()

    assert 150 <= ethan.balance.current_value() <= 325

    with pytest.raises(ValueError):
        chip_col.place_bet(ethan, 5000)


def test_goose_actions() -> None:
    '''
    Тест возможностей гусей: атака, крик, попытка кражи.
    :return: Ничего не возвращает.
    '''
    ethan = users.Player("Ethan", 300)
    boris = users.Goose("Boris")
    denis = users.WarGoose("Denis")
    gosha = users.HonkGoose("Gosha", 0.7)

    boris.steal_attempt(ethan)
    assert 250 <= ethan.balance.current_value() <= 300

    denis.attack(ethan)
    assert 200 <= ethan.balance.current_value() <= 250

    gosha.scream(ethan)
    assert 130 <= ethan.balance.current_value() <= 180

    ivan = users.Player("Ivan", 25)

    gosha.scream(ivan)
    assert ivan.balance.current_value() == 0
    ivan.balance.__setitem__("Ivan", 25)

    denis.attack(ivan)
    assert ivan.balance.current_value() == 0
    ivan.balance.__setitem__("Ivan", 25)

    boris.steal_attempt(ivan)
    assert ivan.balance.current_value() >= 0
