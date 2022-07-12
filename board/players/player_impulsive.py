from players.base_player import BasePlayer


class PlayerImpulsive(BasePlayer):
    """
    The impulsive player buys any property he lands on.
    """
    def _roles_to_payment(self, patrimony):
        self.pay(patrimony.property_price, patrimony.type_of_strategy)
        return True
