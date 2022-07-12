from typing import Counter

from config import settings


def test_quantity_of_properties(board):
    assert len(board) == int(settings['ENV_QUANTITY_OF_PROPERTIES'])


def test_board_walk_on_the_board(board, player_impulsive):
    player_impulsive.position = 19
    assert board.walk_on_the_board(player_impulsive, 1) == 0


def test_board_check_winner(board, player_impulsive):
    for p in board.players:
        if player_impulsive != p:
            p.cash_balance = -1
    _player = board.check_winner(player_impulsive)
    board.winner = _player
    assert board.winner == player_impulsive


def test_board_quantity_of_players(board):
    assert sum(Counter(board.players).values()) == 4


def test_board_roll_dice(board):
    assert board.roll_dice in list(range(1, 7))
    assert type(board.roll_dice) == int
