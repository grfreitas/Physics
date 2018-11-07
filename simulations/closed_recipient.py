import numpy as np
#import itertools
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(10,5))
plt.grid()
points, = ax.plot(0,'o')

ax.set_xlim(0,2)
ax.set_ylim(0,1)
ax.set_xticks(np.linspace(0,2,41))
ax.set_yticks(np.linspace(0,1,21))
for tick in ax.get_xticklabels(): tick.set_rotation(50)

def get_initial_conditions():

	n_particles = 100
	velocity    = 5

	x   = np.random.uniform(0,2,n_particles)
	y   = np.random.uniform(0,1,n_particles)
	phi = np.random.uniform(0,2*np.pi,n_particles)

	v_x = velocity*np.cos(phi)
	v_y = velocity*np.sin(phi)

	return x, y, v_x, v_y

def update(data):
	points.set_xdata(data[0])
	points.set_ydata(data[1])
	points.set_color('r')
	points.set_markersize(6)
	return points,

def generate_points():

	delta_t = 0.001

	R = 0.0025

	x, y, v_x, v_y = get_initial_conditions()

	while True:

		x, y = x + v_x*delta_t, y + v_y*delta_t

		#x_pairs = np.array(list(itertools.combinations(x, 2)))
		#y_pairs = np.array(list(itertools.combinations(y, 2)))
		#x_diff  = np.apply_along_axis(lambda k:k[0]-k[1],1,x_pairs)
		#y_diff  = np.apply_along_axis(lambda k:k[0]-k[1],1,y_pairs)
		#dist    = np.sqrt(x_diff**2 + y_diff**2)
		#ball_collision = np.where(dist <= 2*R)

		x_wall_collision = np.argwhere((x>=2)|(x<=0)).T
		y_wall_collision = np.argwhere((y>=1)|(y<=0)).T
		v_x[x_wall_collision] = -v_x[x_wall_collision]
		v_y[y_wall_collision] = -v_y[y_wall_collision]

		yield [x, y]

ani = animation.FuncAnimation(fig, update, generate_points, interval=5, blit=True)

plt.show()