import matplotlib.pyplot as plt
import random
import time
import numpy as np

def discrete_random_walk(n=1):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1),
                                  (0,-1),
                                  (1, 0),
                                  (-1,0)])
        x += dx
        y += dy
    return (x,y)

for k in range(25):
    plt.figure(figsize=(16,9))
    plt.xticks(range(-100,101))
    plt.yticks(range(-100,101))
    plt.grid(alpha=0.2)
    plt.scatter(0,0,color='black', s=50, marker='+')

    origin = [0],[0]
    pos_x = 0
    pos_y = 0

    steps = 50

    for i in range(steps):

        x, y = discrete_random_walk()

        pos_x += x
        pos_y += y

        plt.quiver(*origin, x, y, 
                    angles='xy', 
                    scale_units='xy', 
                    scale=1, 
                    color='#42BEBA',
                    alpha=0.3)

        origin = np.add(origin[0],x),np.add(origin[1],y)

        plt.title(f'Passos = {i} | Distância de Manhattan: {abs(pos_x)+abs(pos_y)}')
        plt.pause(0.1)

    origin = [0],[0]
    plt.title(f'Passos = {steps} | Distância de Manhattan: {abs(pos_x)+abs(pos_y)}')
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
    plt.pause(0.05)
    time.sleep(2)
    plt.close()

input()
