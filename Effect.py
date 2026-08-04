import pygame

class Effect:
    def __init__(self, duration):
      self.duration = duration

    def apply(self, enemy):
      pass

    def update(self, dt, enemy):
      pass

    def expired(self):
      return self.duration <= 0

class FireEffect(Effect):
  def __init__(self, duration, dps):
    super().__init__(duration)
    self.dps = dps
    self.color_overlay = (255, 80, 0)

  def update(self, dt, enemy):
    enemy.health -= self.dps * dt
    self.duration -= dt
    print(self.duration)

    if self.duration <= 0:
        enemy.color_overlay = None
        return True

    return False
