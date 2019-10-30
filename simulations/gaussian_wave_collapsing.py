import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.constants import hbar, electron_mass


Writer = animation.writers['ffmpeg']
writer = Writer(fps=40, metadata=dict(artist='Gabs'), bitrate=5000)


def psi2(t):
    w = np.sqrt(a / (1 + (2*hbar*a*t/electron_mass)**2))
    return np.sqrt(2/np.pi)*w*np.exp(-2*w**2*x**2)


def animate(t):

    line.set_ydata(psi2(t))

    return line,


def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


a = 500
x = np.linspace(-100, 100, 1000) / a

fig, ax = plt.subplots(1, 1, figsize=(6, 6))

ax.set_ylim(0, psi2(t=0).max() * 1.1)
ax.set_xlabel('x/a')
ax.set_ylabel('|Ψ|²')


line, = ax.plot(x, psi2(t=0), color='black')

ani = animation.FuncAnimation(
    fig,
    animate,
    np.arange(1, 200),
    init_func=init,
    interval=.1,
    blit=True)

ani.save('wave_function.mp4', writer=writer)

# plt.show()
