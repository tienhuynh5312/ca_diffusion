def animDiffusionGray(grids):
    import matplotlib.pyplot as plt
    
    fig1 = plt.figure(figsize=(10,10))
    ax = fig1.add_axes((0, 0, 0.5, 0.5))
    ax.axis('off')
    data = grids[0]
    img = ax.imshow(data, interpolation='gaussian', cmap=plt.cm.rainbow,
                    extent=[0, 28, 0, 20],
                    aspect='auto',
                    zorder=0)
    for it in range(1,len(grids)):
        data = grids[it]
        img.set_data(data)
        plt.draw()
        plt.pause(0.5)
        
    plt.show()
        