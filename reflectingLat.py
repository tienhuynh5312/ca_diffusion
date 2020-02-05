import numpy as np

lat = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
##Reflects the lat
def reflectingLat(lat):
    # Creates array to store original values + reflected boundary 
    rows = len(lat) 
    columns = len(lat[0])
    reflectedLat = np.zeros((rows + 2, columns + 2))
    
    ##Extends left boundary
    for i in range(rows): 
        reflectedLat[i + 1][0] = lat[i][0]
    
    #Extends right boundary
    for i in range(rows): 
        reflectedLat[i + 1][columns + 1] = lat[i][columns - 1]        
    
    #Extends top boundary
    reflectedLat[0][1:-1] = lat[0]
    
    #Copies original grid
    for i in range(len(lat)):
        reflectedLat[i + 1][1:-1] = lat[i]
    
    #Extends bottom boundary 
    reflectedLat[rows + 1][1:-1] = lat[rows - 1]
    
    #Extends Corners 
    reflectedLat[0][0] = reflectedLat[1][0]
    reflectedLat[0][columns + 1] = reflectedLat[1][columns + 1]
    reflectedLat[rows + 1][columns + 1] = reflectedLat[rows][columns + 1]
    reflectedLat[rows + 1][0]  = reflectedLat[rows][0]
    
    return reflectedLat     