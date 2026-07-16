class Effect:
  def __init__(self, effect_type, duration, dps):
    self.effect_type
    self.duration = duration
    self.timer = 0
    self.dps = dps

  def expired(self):
    return self.timer >= self.duration

  def get_damage(self, target, dt):
    if self.effect_type = "poison":
      return self.dps
      
    if self.effect_type = "burn":
      return self.dps
    
    return 0
  
  
  
