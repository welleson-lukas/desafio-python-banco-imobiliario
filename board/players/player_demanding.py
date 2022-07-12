from players.base_player import BasePlayer


class PlayerDemanding(BasePlayer):
    """
    The demanding player buys any property as long as its rent is greater than 50.
    """
    def _roles_to_payment(self, patrimony):
        if patrimony.rental_price > 50:
            self.pay(patrimony.property_price, patrimony.type_of_strategy)
            return True
        return False
