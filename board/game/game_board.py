from datetime import datetime
from random import randint

from config import settings
from game.patrimony import Patrimony


class GameBoard:

    def __init__(self, *args, **kwargs):
        self._winner = None
        self._played = 0
        self._players = []
        self.start_time = datetime.now()
        self._cards = [
            Patrimony(index, None)
            for index in range(int(settings['ENV_QUANTITY_OF_PROPERTIES']))
        ]

    @property
    def played(self):
        return self._played

    @played.setter
    def played(self, played):
        self._played = played

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, players):
        self._players = players

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, winner):
        self._winner = winner

    @property
    def roll_dice(self):
        """
        The player rolls a 6-sided equiprobable die that determines
        how many spaces on the board the player will move.
        """
        return randint(1, 6)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, patrimony):
        self._cards[position] = patrimony

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"

    def __repr__(self):
        return f"{self._cards}"

    def remove_player(self, player):
        for patrimony in self._cards:
            if patrimony.type_of_strategy == player:
                patrimony.type_of_strategy = None
        self._players.remove(player)

    def walk_on_the_board(self, player, _dice=None):
        """
        When completing a turn on the board, the player gains 100 balance.
        """
        go_to_position = player.position + (_dice or self.roll_dice)
        if go_to_position >= int(settings['ENV_QUANTITY_OF_PROPERTIES']):
            player.cash_balance += float(settings['ENV_PLAYER_MONEY_ROUND'])
            go_to_position -= int(settings['ENV_QUANTITY_OF_PROPERTIES'])
        player.position = go_to_position
        return go_to_position

    def check_winner(self, player):
        """
        It ends when there is only one player left with a positive balance at any time during the game.
        That player is declared the winner.
        """
        if len(self.players) == 1:
            return player
        if int(settings['ENV_TIMEOUT_ROUND']) <= self.played:
            cash_balance = 0
            winner = None
            for _player in self._players:
                if _player.cash_balance > cash_balance:
                    cash_balance = _player.cash_balance
                    winner = _player
            return winner

        elements = [
            _player.cash_balance
            for _player in self._players if _player != player
        ]
        if sum(elements) < 0:
            return player

        return None

    def play(self, player):
        """
        A player with a negative balance loses the game and no longer plays.
        It loses its properties and therefore can be purchased by any other player.
        """
        if player.cash_balance <= 0:
            player.gameover = True
            return

        patrimony = self._cards[self.walk_on_the_board(player)]
        player.rent_or_sale(patrimony)

    def finish(self):
        return {
            "time_it": (datetime.now() - self.start_time).total_seconds(),
            "winner": self.winner,
            "cash_balance": self.winner.cash_balance,
            "played": self.played,
            "strategy": self.winner,
            "time_out": self.played > int(settings['ENV_TIMEOUT_ROUND']),
        }
