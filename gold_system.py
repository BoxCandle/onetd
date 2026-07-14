class GoldSystem:
    def __init__(self, player_gold):
        self.player_gold = player_gold

    def add_gold(self, gold_amount):
        self.player_gold += gold_amount
        return self.player_gold