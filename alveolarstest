import matplotlib.pyplot as plt


class one_alveolar:
  def __init__ (self, impedance, VoltoP, timestep, restime,inpressure, initialvolume = 1):
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
    if deltavol>0 and deltavol< 0.02:
      self.inp = 0
    #end expiration change
    if self.restime-self.looptime<0.01:
      self.looptime = 0
      self.inp = self.inpressure


def VolP(vol):
	return vol*1.2

alvs = []
for i in range(100):
    alvs.append(one_alveolar(1,VolP,0.1,15,10,1))

vol = []
baseline = []

for i in range(500):
  totalvol = 0
  for alv in alvs:
    totalvol += alv.volume
    alv.update()
  baseline.append(0)
  vol.append(totalvol)

plt.plot(range(500),baseline,'k')
plt.plot(range(500),vol,'r')
plt.show()
