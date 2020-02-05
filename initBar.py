from applyDiffusionExtended import applyDiffusionExtended
from reflectingLat import reflectingLat 
from animDiffusionGray import animDiffusionGray 

AMBIENT = 25
HOT = 100
COLD = 10

hotSites = [(5,5)]
coldSites = [(2,2),(7,7)]

t = 50
diffusionRate = 0.01
def initBar(m, n, hotSites, coldSites):
    import numpy as np
    
    #- Init bar
    site = np.full((m,n), AMBIENT)
    
    return applyHotCold(site, hotSites, coldSites)

def applyHotCold(site, hotSites, coldSites):
    #- apple hot 
    for i in hotSites:
        site[i[0],i[1]] = HOT
    
    for i in coldSites:
        site[i[0],i[1]] = COLD
    
    return site

def diffusionSim(m,n, diffusionRate, t):
    bar = initBar(m,n, hotSites, coldSites)
    grids = [bar]
    for i in range(t):
        barExtended = reflectingLat(bar)
        bar = applyDiffusionExtended(diffusionRate, barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        grids.append(bar)
        
    return grids

