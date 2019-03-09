class one_alveolar:
  #impedance: 顺应性
  #voltop:volum relations to pressure
  #timestep: time increases each time
  def __init__ (self, impedance, VoltoP, timestep, restime, intime, inpressure, initialvolume = 1):
    self.initialvolume = initialvolume
    self.volume = self.initialvolume
    self.impedance = impedance
    self.inpressure = inpressure
    self.isin = True
    self.VoltoP = VoltoP
    self.timestep = timestep
    self.flowvelo = 0
    self.inp = self.inpressure
    self.restime = restime
    self.intime = intime
    self.looptime = 0
    
  def update(self):
    self.alvp = self.VoltoP(self.volume) - self.initialvolume
    self.flowvelo = (self.inp - self.alvp)/self.impedance
    deltavol = self.flowvelo*self.timestep
    self.volume += deltavol
    self.looptime += self.timestep
    #inspiration and expiration change section
    #auto interchange
    #if abs(deltavol) < 0.02:
    #    self.inp = 0 if self.isin == True else self.inpressure
    #    self.isin = True if not self.isin else False
    #end inspiration change
    if deltavol>0 and deltavol< 0.02 and self.looptime>self.intime:
      self.inp = 0
    #end expiration change
    if self.restime-self.looptime<0.01:
      self.looptime = 0
      self.inp = self.inpressure
