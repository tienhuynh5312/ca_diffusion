import numpy as np
import Diffusion.py as d

#Returns the lattice with extended boundary removed,
# and applys diffusion to all cells
def applyDiffusionExtended(latExt, diffusionRate): 
    diffused = np.zeros(len(latExt) - 2, len(latExt[0]) - 2)
    for i in range(1, len(latExt) - 1): 
        for j in range(1, len(latExt[0]) - 1): 
            site = latExt[i][j]
            N = latExt[i - 1][j]
            NE = latExt[i - 1][j + 1]
            E = latExt[i][j + 1]
            SE = latExt[i + 1][j + 1]
            S = latExt[i + 1][j]
            SW = latExt[i + 1][j - 1]
            W = latExt[i][j - 1]
            NW = latExt[i - 1][j - 1]
            diffused[i - 1][j - 1] = d.diffusion(latExt[i][j], site, N, NE, SE, S, SW, W, NW)
    return diffused 