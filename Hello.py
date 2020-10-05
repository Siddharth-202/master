import math
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0,25,1)
y1 = map(math.sin,math.pi*t)
y2 = map(math.sin,math.pi*t+math.pi/2)
y3 = map(math.sin,math.pi*t-math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.show()