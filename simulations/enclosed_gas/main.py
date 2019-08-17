import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BOX_WIDTH = 6.0
BOX_HEIGHT = 1.0

FPS = 60
TIME_DELTA = .02


class Particle(object):

    def __init__(self, **kwargs):

        self.position = np.array([np.random.uniform(-BOX_WIDTH, +BOX_WIDTH), np.random.uniform(-BOX_HEIGHT, +BOX_HEIGHT)])
        self.velocity = np.array([np.random.uniform(-2, 2), np.random.uniform(-2, 2)])
        self.acceleration = np.array([0.0, 0.0])

        self.mass = np.random.uniform(1, 100)
        self.radius = 0.015
        self.index = kwargs.get('index')

        self.__check_particles_collision = np.vectorize(self.__check_particle_collision, otypes=[None])

    def __check_wall_collision(self):

        if abs(self.position[0]) > BOX_WIDTH:
            self.position[0] = round(self.position[0])
            self.velocity[0] *= -1

        if abs(self.position[1]) > BOX_HEIGHT:
            self.position[1] = round(self.position[1])
            self.velocity[1] *= -1

    def __check_particle_collision(self, other):

        dx, dy = self.position - other.position
        d = np.sqrt(dx ** 2 + dy ** 2)

        limit_distance = self.radius + other.radius

        if 0 < d < limit_distance:

            delta_self = np.dot(self.velocity - other.velocity, self.position - other.position) \
                    * (self.position - other.position) / d ** 2 \
                    * (2 * other.mass / (self.mass + other.mass))

            self.velocity = self.velocity - delta_self
            other.velocity = other.velocity + delta_self

    def update_velocity(self, particles):

        self.__check_wall_collision()
        self.__check_particles_collision(particles)

        self.velocity += self.acceleration * TIME_DELTA

    def update_position(self):

        self.position += self.velocity * TIME_DELTA


def animate(particles):

    pos = np.array([particle.position for particle in particles])
    x, y = pos[:, 0], pos[:, 1]

    points.set_xdata(x)
    points.set_ydata(y)

    return points,


def get_initial_state(n=100):

    particles = [Particle(index=i) for i in range(n)]

    for particle in particles:
        particle.acceleration[1] = - 9

    return particles


def run_simulation():

    particles = get_initial_state()

    def update_state(particle, system):

        particle.update_velocity(system)
        particle.update_position()

    update_state = np.vectorize(pyfunc=update_state, excluded=['system'], otypes=[None])

    while True:

        update_state(particles, system=particles)

        yield particles


def main():

    global points
    global ax

    fig, ax = plt.subplots(1, 1, figsize=(BOX_WIDTH * 5, BOX_HEIGHT * 5))

    ax.set_xlim(-BOX_WIDTH, +BOX_WIDTH)
    ax.set_ylim(-BOX_HEIGHT, +BOX_HEIGHT)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.axhline(0, ls='--', lw=1.5, color='k')

    points, = ax.plot(0, 'o', ms=2, color='red')

    ani = animation.FuncAnimation(fig, animate, run_simulation, interval=0, blit=True)
    plt.show(ani)

    return


if __name__ == '__main__':
    main()
