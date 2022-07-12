from players.base_player import BasePlayer


class PlayerCautious(BasePlayer):
    """
    The cautious player buys any property as long as he has a
    reserve of 80 balances remaining after the purchase.
    """
    def _roles_to_payment(self, patrimony):
        if (self.cash_balance - patrimony.property_price) >= 80:
            self.pay(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
