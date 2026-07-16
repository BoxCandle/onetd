class Effect:
  def __init__(self, effect_type, duration, dps):
    data = EFFECTS[effect_type]
    
    self.type = effect_type
    self.duration = data["duration"]
    self.dps = data["dps"]
    self.timer = 0

  def expired(self):
    return self.timer >= self.duration

  def get_damage(self, target, dt):
    if self.effect_type = "poison":
      return self.dps
      
    if self.effect_type = "burn":
      return self.dps
    
    return 0
  
  
  
