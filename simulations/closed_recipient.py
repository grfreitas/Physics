import numpy as np
from numpy import cos, sin

import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import pandas as pd

fig, ax = plt.subplots(figsize=(6,6))
plt.grid()
points = ax.plot(0,'o')[0]

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xticks(np.linspace(0,1,21))
ax.set_yticks(np.linspace(0,1,21))
for tick in ax.get_xticklabels(): tick.set_rotation(50)

def get_initial_conditions():

	N = 5
	mass = [1]*N
	radius = [.05]*N
	velocity = 5

	x   = np.random.uniform(0, 1, N)
	y   = np.random.uniform(0, 1, N)
	phi	= np.random.uniform(0, 2*np.pi, N)

	v_x = velocity*cos(phi)
	v_y = velocity*sin(phi)

	x_diffs = np.apply_along_axis(lambda f: f[0]-f[1], 1, np.array(list(itertools.permutations(x, 2))))
	y_diffs = np.apply_along_axis(lambda f: f[0]-f[1], 1, np.array(list(itertools.permutations(y, 2))))
	dists = np.split(np.insert(np.sqrt(y_diffs**2 + x_diffs**2), range(0, N**2, N), 0), N)

	system_initial_state = np.hstack((np.dstack((x, y, v_x, v_y, phi, mass, radius))[0], dists))

	return N, system_initial_state

def update(data):
	points.set_xdata(data[0])
	points.set_ydata(data[1])
	points.set_color('r')
	points.set_markersize(8)
	return points,

def calc_dif(pos):
	return pos[0]-pos[1]

def update_xy(states):
	delta_t = 0.0005
	states[:,0] = states[:,0] + states[:,2]*delta_t
	states[:,1] = states[:,1] + states[:,3]*delta_t

def update_dists(states):
	x_diffs = np.apply_along_axis(calc_dif, 1, np.array(list(itertools.permutations(states[:,0], 2))))
	y_diffs = np.apply_along_axis(calc_dif, 1, np.array(list(itertools.permutations(states[:,1], 2))))
	states[:,7:] = np.split(np.insert(np.sqrt(y_diffs**2+x_diffs**2),range(0, len(states)**2,len(states)),0), len(states))

def check_wall_collision(states):
	x_wall_collision = np.argwhere((states[:,0]>=1)|(states[:,0]<=0)).T
	y_wall_collision = np.argwhere((states[:,1]>=1)|(states[:,1]<=0)).T
	states[:,2][x_wall_collision] = -states[:,2][x_wall_collision]
	states[:,3][y_wall_collision] = -states[:,3][y_wall_collision]

def check_ball_collision(states):

	check = np.argwhere(states[:,7:]<0.1).T
	duplicate = np.argwhere((check[1]-check[0])==0).flatten()
	collided = np.array([np.delete(check[0], duplicate), np.delete(check[1], duplicate)]).T

	if len(states[collided]) > 0:
		print(states[collided])
		print('-'*10)
		dx = np.apply_along_axis(calc_dif, 1, states[:,0][collided])
		dy = np.apply_along_axis(calc_dif, 1, states[:,1][collided])
		d = np.sqrt(np.power(dx, 2) + np.power(dy, 2))

		nx = dx / d
		ny = dy / d

		v1x = states[:,2][collided][:,0]
		v1y = states[:,3][collided][:,0]
		v2x = states[:,2][collided][:,1]
		v2y = states[:,3][collided][:,1]

		p = 2*(v1x*nx + v1y*ny - v2x*nx - v2y*ny)/2;

		states[:,2][collided][:,0] = v1x - p * nx;
		states[:,3][collided][:,0] = v1y - p * ny;
		states[:,2][collided][:,1] = v2x + p * nx;
		states[:,3][collided][:,1] = v2y + p * ny;

		print(states[collided])

	print('='*10)
	return

def make_simulation():

	N, states = get_initial_conditions()

	while True:

		check_ball_collision(states)
		check_wall_collision(states)

		update_xy(states)
		update_dists(states)

		yield [states[:,0], states[:,1]]

ani = animation.FuncAnimation(fig, update, make_simulation, interval=5, blit=True)
plt.show()
