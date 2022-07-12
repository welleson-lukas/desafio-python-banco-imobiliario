from random import randint

from players.base_player import BasePlayer


class PlayerRandom(BasePlayer):
    """
    The random player buys the property he lands at the over with a 50% probability.
    """
    def _roles_to_payment(self, patrimony):
        if randint(0, 1) > 0:
            self.pay(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
