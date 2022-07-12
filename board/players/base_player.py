from abc import ABC, abstractmethod

from config import settings


class BasePlayer(ABC):

    def __init__(
            self,
            strategy,
            position=0,
            cash_balance=float(settings['ENV_PLAYER_MONEY'])):

        self.position = position
        self.cash_balance = cash_balance
        self.strategy = strategy
        self.gameover = False

    def __str__(self):
        return f"{self.strategy}"

    def __repr__(self):
        return f"{self.strategy}"

    def rent_or_sale(self, patrimony):
        if patrimony.type_of_strategy:
            if self != patrimony.type_of_strategy:
                self.pay(patrimony.rental_price, patrimony.type_of_strategy)
            return

        if self._roles_to_payment(patrimony):
            patrimony.type_of_strategy = self

    @abstractmethod
    def _roles_to_payment(self, patrimony):
        raise NotImplementedError()

    def pay(self, property_price, type_of_strategy=None):
        self.cash_balance -= property_price
        if type_of_strategy:
            type_of_strategy.cash_balance += property_price
        if not self.cash_balance:
            self.gameover = True
