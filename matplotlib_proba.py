#git clone https://github.com/pepaSuli/python2022.git

#pip install matplotlib --proxy http://tanulo01:Tanulo0118@172.16.0.5:8080
#python -m pip install matplotlib --proxy http://tanulo01:Tanulo0118@172.16.0.5:8080

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 16])
ypoints = np.array([0, 25])

#plt.plot(xpoints, ypoints)
#plt.plot([10,20,12],[32,10,12])


x=[0,50,50,0,0]
y=[0,0,50,50,0]
plt.plot(x, y)


plt.show()
