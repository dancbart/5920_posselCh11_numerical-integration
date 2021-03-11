import numpy as np
import matplotlib.pyplot as plt

## 11.1 Step-by-step numerical integration: Euler method

#Constants
k = 0.5
m = 1.0
numberOfSteps = 30000
DeltaT = 0.001

#This is how we parse out time for horizontal axis
tCollector=np.linspace(0,numberOfSteps*DeltaT, numberOfSteps+1)

#this is basically a "theoretical" calculation of the solution to the differential equation.
#It's just a sine curve.  We will plot x_theo + y_theo on the same graph as xCollector + vCollector.
#If they lay directly on top of eachother, this indicates a nice fit (i.e. we got the mathematics correct, AND we put in enough steps 30,000)
x_theo = np.arange(np.pi*9.54929658552,DeltaT)
y_theo = np.cos(((k/m)**.5)*x_theo)

# Initial Conditions for numerical calculations
xCollector=[1.0]
vCollector=[0]
for ii in range(numberOfSteps):
    xNew = xCollector[-1] + vCollector[-1]*DeltaT
    vNew = vCollector[-1] + (-k/m*xCollector[-1])*DeltaT
    xCollector.append(xNew)
    vCollector.append(vNew)

#plt.plot(tCollector,xCollector)
#plt.plot(x_theo,y_theo)

# 11.2 Numerical errors

diff = xCollector-y_theo
print (diff)

plt.plot (tCollector,diff)

#fig = plt.figure()
#ax = fig.add_subplot()
#ax.set_title('Chap11 possel',pad=20)
#ax.plot(tCollector,diff)
