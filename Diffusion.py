__author__ = 'v-caearl'

def diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    import numpy as np
    neighbors = np.array([N,NE,E,SE,S,SW,W,NW])
    tmp = np.abs(np.random.normal(0,0.5,8))
    adjustRate = tmp/np.sum(tmp)
    randomRate = (1+adjustRate)*diffusionRate
    result = site + np.sum(randomRate*(neighbors-site))
    return result
