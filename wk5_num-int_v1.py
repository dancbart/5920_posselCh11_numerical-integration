import numpy as np
import matplotlib.pyplot as plt

k = 0.5
m = 1.0
numberOfSteps = 30000
DeltaT + 0.001

tCollector=np.linspace(0,numberOfSteps*DeltaT, numberOfSteps+1)

# Initial Conditions
x_theo = np.arange(np.pi*9.54929658552,DeltaT)
y_theo = np.cos(((k/m)**.5)*x_theo)

xCollector=[1.0]
vCollector=[0]
for ii in range(numberOfSteps):
    xNew = xCollector[-1] + vCollector[-1]*DeltaT
    vNew = vCollector[-1] + (-k/m*xCollector[-1])*DeltaT
    xCollector.append(xNew)
    vCollector.append(vNew)

plt.plot(tCollector,xCollector)
plt.plot(x_theo,y_theo)
