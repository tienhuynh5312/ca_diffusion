def animDiffusionGray(grids):
    import matplotlib.pyplot as plt
    import numpy as np
    fig1 = plt.figure(figsize=(10,10))
    ax = fig1.add_axes((0, 0, 0.5, 0.5))
    ax.axis('off')
    data = grids[0]
    img = ax.imshow(data, interpolation='None', cmap=plt.cm.RdBu_r,
                    extent=[0, np.min(data), 0, np.max(data)],
                    aspect='auto',
                    zorder=0)
    for it in range(1,len(grids)):
        data = grids[it]
        img.set_data(data)
        plt.draw()
        plt.pause(0.5)
        
    plt.show()
        