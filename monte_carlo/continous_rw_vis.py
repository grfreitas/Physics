import matplotlib.pyplot as plt
import random
import time
import numpy as np

def continuous_random_walk(n=1):

    r_0, theta_0 = 0, 0
    
    for i in range(n):
        theta = random.uniform(0,2*np.pi)
        r = np.sqrt(1 + r_0**2 + 2*r_0*np.cos(theta-theta_0))
        theta_0 = theta_0 + np.arctan2(np.sin(theta-theta_0), r_0 + np.cos(theta-theta_0))
        r_0 = r

    return r, theta_0

for k in range(10):
    plt.figure(figsize=(6,6))
    plt.xticks(range(-100,101))
    plt.yticks(range(-100,101))
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.grid(alpha=0.2)
    plt.scatter(0,0,color='black', s=50, marker='+')

    circle1 = plt.Circle((0, 0), 1, color='r', fill=False)

    fig = plt.gcf()
    ax = fig.gca()

    ax.add_artist(circle1)

    origin = [0],[0]
    pos_x = 0
    pos_y = 0

    steps = 3

    for i in range(steps):

        r, theta = continuous_random_walk()

        x = r*np.cos(theta)
        y = r*np.sin(theta)

        pos_x += x
        pos_y += y

        plt.quiver(*origin, x, y, 
                    angles='xy', 
                    scale_units='xy', 
                    scale=1, 
                    color='#42BEBA',
                    alpha=0.3)

        origin = np.add(origin[0],x),np.add(origin[1],y)

        plt.title(f'Passos = {i} | Distância Radial: {round(np.sqrt(pos_x**2+pos_y**2),2)}')
        plt.pause(1)

    origin = [0],[0]
    plt.title(f'Passos = {steps} | Distância Radial: {round(np.sqrt(pos_x**2+pos_y**2),2)}')
    plt.quiver(*origin, pos_x, pos_y, 
                angles='xy', 
                scale_units='xy', 
                scale=1, 
                color='darkgray',
                alpha=0.7)
    if (pos_x == 0) & (pos_y == 0):
        plt.scatter(0,0,color='red', s=30)
    else: 
        plt.scatter(0,0,color='black', s=50, marker='+')
    plt.pause(1)
    time.sleep(2)
    plt.close()

input()
