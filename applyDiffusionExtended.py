import numpy as np

from Diffusion import diffusion
#Returns the lattice with extended boundary removed,
# and applys diffusion to all cells
def applyDiffusionExtended(diffusionRate, latExt): 
    row_num = np.shape(latExt)[0]
    col_num = np.shape(latExt)[1] 
    diffused = np.zeros((row_num - 2, col_num - 2))
    for i in range(1, row_num - 1): 
        for j in range(1, col_num - 1): 
            site = latExt[i,j]
            N = latExt[i-1,j]
            NE = latExt[i-1,j+1]
            E = latExt[i,j+1]
            SE = latExt[i+1,j+1]
            S = latExt[i+1,j]
            SW = latExt[i+1,j-1]
            W = latExt[i,j-1]
            NW = latExt[i-1,j-1]
            diffused[i-1,j-1] = diffusion(diffusionRate, site, N, NE, E, SE, S, SW, W, NW)
    return diffused 
