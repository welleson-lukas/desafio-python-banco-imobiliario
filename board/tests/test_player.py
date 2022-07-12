from game.patrimony import Patrimony


def test_sale_patrimony_player_impulsive(player_impulsive):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price = 100
    player_impulsive.rent_or_sale(patrimony)
    assert player_impulsive.cash_balance >= 200
    assert not player_impulsive.gameover


def test_sale_patrimony_player_cautious(player_cautious):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price = 100
    player_cautious.rent_or_sale(patrimony)
    assert player_cautious.cash_balance >= 80
    assert not player_cautious.gameover


def test_sale_patrimony_player_random(player_randomer):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price = 90
    player_randomer.rent_or_sale(patrimony)
    assert player_randomer.cash_balance >= 200
    assert not player_randomer.gameover


def test_sale_patrimony_player_demanding(player_demanding):
    patrimony = Patrimony(0, type_of_strategy=None)
    patrimony.property_price = 50
    player_demanding.rent_or_sale(patrimony)
    assert player_demanding.cash_balance >= 200
    assert not player_demanding.gameover
