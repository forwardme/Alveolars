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

high_impedance_alvs = []
medium_impedance_alvs = []
low_impedance_alvs = []
lung = [high_impedance_alvs,medium_impedance_alvs,low_impedance_alvs]

for i in range(100):
    high_impedance_alvs.append(one_alveolar(6,VolP,0.1,30,10,1))
    medium_impedance_alvs.append(one_alveolar(3,VolP,0.1,30,10,1))
    low_impedance_alvs.append(one_alveolar(1,VolP,0.1,30,10,1))


totalvol = []
high_impedance_vol = []
medium_impedance_vol =[]
low_impedance_vol = []
baseline = []
high_impedance_alvp = []
medium_impedance_alvp = []
low_impedance_alvp = []
meanalvp = []
for i in range(500):
    addvol = 0
    for alv in high_impedance_alvs:
      addvol += alv.volume
      alv.update()
    high_impedance_vol.append(addvol)
    high_impedance_alvp.append(high_impedance_alvs[0].alvp)
    addvol = 0
    for alv in medium_impedance_alvs:
      addvol += alv.volume
      alv.update()
    medium_impedance_vol.append(addvol)
    medium_impedance_alvp.append(medium_impedance_alvs[0].alvp)
    addvol = 0
    for alv in low_impedance_alvs:
      addvol += alv.volume
      alv.update()
    low_impedance_vol.append(addvol)
    low_impedance_alvp.append(low_impedance_alvs[0].alvp)
    meanalvp.append((high_impedance_alvs[0].alvp + medium_impedance_alvs[0].alvp + low_impedance_alvs[0].alvp)/3)
    baseline.append(0)

plt.plot(range(500),baseline,'k')
#plt.plot(range(500),high_impedance_vol,'r')
#plt.plot(range(500),medium_impedance_vol,'g')
#plt.plot(range(500),low_impedance_vol,'b')
plt.plot(range(500),high_impedance_alvp,'c')
plt.plot(range(500),medium_impedance_alvp,'m')
plt.plot(range(500),low_impedance_alvp,'y')
plt.plot(range(500),meanalvp,'r')
plt.show()
