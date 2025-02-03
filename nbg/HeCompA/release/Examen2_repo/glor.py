

def plot_trayectorias(fig, track_1, track_2):
    ax1 = fig.add_subplot(1, 2, 1, projection='3d',title='Espacio fase $xyz$')
    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')
    ax1.set_zlabel('$z$')
    # Graficamos las condiciones iniciales (verdes)
    ax1.scatter(track_1[0,0], track_1[1,0], track_1[2,0], fc='green', ec='k', s = 50, zorder=10) 
    ax1.scatter(track_2[0,0], track_2[1,0], track_2[2,0], fc='green', ec='k', s = 50, zorder=10) 
    # Graficamos las trayectorias
    ax1.plot(track_1[0,:], track_1[1,:], track_1[2,:], '-', lw=0.75)
    ax1.plot(track_2[0,:], track_2[1,:], track_2[2,:], '-', lw=0.75)
    # Graficamos las posiciones finales (rojas)
    ax1.scatter(track_1[0,-1], track_1[1,-1], track_1[2,-1], fc='red', ec='k', s = 50, zorder=5) 
    ax1.scatter(track_2[0,-1], track_2[1,-1], track_2[2,-1], fc='red', ec='k', s = 50, zorder=5) 
    
    ax2 = fig.add_subplot(1, 2, 2, title='Plano fase $xz$')
    ax2.set_xlabel('$x$')
    ax2.set_ylabel('$z$')
    # Graficamos las condiciones iniciales (verdes)
    ax2.scatter(track_1[0,0], track_1[2,0], fc='green', ec='k', s = 50, zorder=10) 
    ax2.scatter(track_2[0,0], track_2[2,0], fc='green', ec='k', s = 50, zorder=10) 
    # Graficamos las trayectorias
    ax2.plot(track_1[0,:], track_1[2,:], '-', lw=0.75)
    ax2.plot(track_2[0,:], track_2[2,:], '-', lw=0.75)
    # Graficamos las posiciones finales (rojas)
    ax2.scatter(track_1[0,-1], track_1[2,-1], fc='red', ec='k', s = 50, zorder=5) 
    ax2.scatter(track_2[0,-1], track_2[2,-1], fc='red', ec='k', s = 50, zorder=5) 