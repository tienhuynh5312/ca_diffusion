def animDiffusionGray(grids):
    import matplotlib.pyplot as plt
    import numpy as np
    fig1 = plt.figure(figsize=(6,6))
    ax = fig1.add_axes((0, 0, 1, 1))
    ax.axis('off')
    data = grids[0]
    img = ax.imshow(data,interpolation='none',cmap=plt.cm.binary,aspect='auto',zorder=0)
    plt.draw()
    for it in range(1,len(grids)):
        data = grids[it]
        img.set_data(data)
        plt.draw()
        plt.pause(0.01)
       
        
    
        
