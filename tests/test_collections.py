import pytest
from src.collections import PlayerCollection, GooseCollection
from src import users


def test_both_collections() -> None:
    '''
    Тест пользовательских коллекций (кроме коллекций ставок). Включает тесты индексации и срезов.
    :return: Ничего не возвращает.
    '''
    player_col: PlayerCollection = PlayerCollection()
    goose_col: GooseCollection = GooseCollection()

    ethan = users.Player("Ethan", 250)
    boris = users.Goose("Boris")
    denis = users.WarGoose("Denis")
    gosha = users.HonkGoose("Gosha", 0.7)

    player_col.add(ethan)
    with pytest.raises(TypeError):
        player_col.add(boris)
    with pytest.raises(TypeError):
        player_col.add(denis)
    with pytest.raises(TypeError):
        player_col.add(gosha)

    with pytest.raises(TypeError):
        goose_col.add(ethan)

    goose_col.add(boris)
    goose_col.add(denis)
    goose_col.add(gosha)

    assert player_col.show() == "Ethan: 250"
    assert goose_col.show() == "Boris: 0.1\nDenis: 0.1\nGosha: 0.7"


    goose_col.remove(gosha)
    assert goose_col.show() == "Boris: 0.1\nDenis: 0.1"
    with pytest.raises(IndexError):
        goose_col.remove(gosha)

    player_col.remove(ethan)
    assert player_col.show() == "Currently no players"
    with pytest.raises(IndexError):
        player_col.remove(ethan)
    player_col.add(ethan)
    goose_col.add(gosha)


    assert player_col.__index__(0) == "Ethan: 250"
    with pytest.raises(IndexError):
        player_col.__index__(1)

    assert goose_col.__index__(2) == "Gosha: 0.7"
    with pytest.raises(IndexError):
        goose_col.__index__(5)

    assert goose_col.__getitem__(slice(0, 2)) == [boris, denis]
    assert player_col.__getitem__(0) == ethan
    with pytest.raises(IndexError):
        goose_col.__getitem__(slice(3, 15))
    with pytest.raises(IndexError):
        goose_col.__getitem__(slice(15, 3))
