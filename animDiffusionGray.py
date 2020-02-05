def animDiffusionGray(grids):
    data = grids[0]
    img = ax.imshow(data, interpolation='none', cmap=plt.cm.rainbow,
                    extent=[0, 28, 0, 20],
                    aspect='auto',
                    zorder=0)
    for it in range(len(grids)):
        data = grids[it]
        img.set_data(data)
        plt.draw()
        plt.pause(0.05)
    return 0