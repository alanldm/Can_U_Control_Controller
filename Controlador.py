import numpy as np
import Velocidades
import Parametros

def calc_traj(player_x, player_y, target_x, target_y, tmp, u, num_p, land, level):
    t = np.arange(tmp, tmp*num_p, tmp)
    px = player_x
    py = player_y
    dMinTraj = 1000000.0
    for dt in t:
        v = Velocidades.vector_vel(px, py, u, land, level)
        #x(t+dt) = x(t) + v*dt
        px = px + v[0]*dt
        py = py + v[1]*dt
        d = np.sqrt((target_x-px)**2+(target_y-py)**2)

        if(d < dMinTraj):
            dMinTraj = d
    
    return dMinTraj

def limita(val):
    '''Restringir um valor entre um valor mínimo e máximo, no caso, entre 1 e -1'''
    return min(1, max(-1, val))

def calc_u(received, u_prev):
    land = received[1]
    level = received[2]
    du, tmp, num_p, filter = Parametros.best_parameters(land, level)
    player_x = received[3]
    player_y = received[4]
    u_new = np.arange(-1, 1, du)

    if (abs(player_x)>0.95 or abs(player_y)>0.95): #Se saiu da tela, tenta voltar para os centro do mapa.
        target_x = 0.0
        target_y = 0.0
    else:
        if (len(received)>8 and (land!=1) and (land!=2) and (land!=4 and (level!=3))):
            if(len(received)==10+2*(received[0]-1)): #Tratamento das caveiras.
                target_x = received[5]
                target_y = received[6]
            else:
                target_x = received[7]
                target_y = received[8]
        else:
            target_x = received[5]
            target_y = received[6]

    dBest = 1000000.0
    uBest = 0.0
    for u in u_new:
        dMinTraj = calc_traj(player_x, player_y, target_x, target_y, tmp, u, num_p, land, level)

        if(dMinTraj < dBest):
            dBest = dMinTraj
            uBest = u

    u = limita(filter*u_prev + (1-filter)*uBest)
    return u