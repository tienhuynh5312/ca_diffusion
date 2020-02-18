from animDiffusionGray import animDiffusionGray
from applyDiffusionExtended import applyDiffusionExtended
from Diffusion import diffusion
from reflectingLat import reflectingLat
from initBar import *
AMBIENT = 25
HOT = 100
COLD = 0

t = 1000
diffusionRate = 0.01

m=10
n=10

animDiffusionGray(diffusionSim(m,n, diffusionRate, t))
print("done")
