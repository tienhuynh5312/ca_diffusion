from animDiffusionGray import animDiffusionGray
from applyDiffusionExtended import applyDiffusionExtended
from Diffusion import diffusion
from reflectingLat import reflectingLat
from initBar import *

import numpy as np
AMBIENT = 25
HOT = 200
COLD = 0

t = 100
diffusionRate = 0.01

m=10
n=10

number_of_sims = 100
grids = np.empty((number_of_sims, t+1, m,n))
average = np.empty((number_of_sims,m,n))
for i in range(number_of_sims):
    grids[i] = diffusionSim(m,n, diffusionRate, t)
    average[i] = np.average(grids[i], axis = 0)
    #- animDiffusionGray(grid)

print(np.average(average, axis = 0))
import matplotlib.pyplot as plt
plt.imshow(np.average(average, axis = 0), cmap=plt.cm.binary,aspect='auto',zorder=0)
plt.show()
print("done")
