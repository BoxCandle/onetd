class LevelSystem:
    def __init__(self, tower, enemy):
        self.tower_xp = tower.xp
        self.xp_amount = enemy.xp_reward
        self.tower_level = tower.level

    def try_level_up(self) -> bool:
        next_level = self.tower_level + 1
        xp_needed = self.xp_required_for(next_level)

        if self.tower_xp < xp_needed:
            return self.tower_level

        self.tower_level = next_level
        print("Level up")
        print("total xp", self.tower_xp)
        return self.tower_level

    def add_xp(self, amount):
        self.tower_xp += amount
        self.try_level_up()
        return self.tower_xp

    def xp_required_for(self, level: int) -> int:
        return 5 * level ** 2