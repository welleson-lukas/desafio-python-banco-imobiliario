import pytest

from config import settings
from game.factory import create_board, create_player


@pytest.fixture(scope='session', autouse=True)
def set_test_settings():
    settings.configure(ENV_FOR_DYNACONF='testing')


@pytest.fixture
def board(set_test_settings):
    return create_board()


@pytest.fixture
def player_impulsive():
    return create_player('impulsivo')


@pytest.fixture
def player_demanding():
    return create_player('exigente')


@pytest.fixture
def player_cautious():
    return create_player('cauteloso')


@pytest.fixture
def player_randomer():
    return create_player('aleatório')
