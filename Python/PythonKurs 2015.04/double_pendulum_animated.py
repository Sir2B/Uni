# coding=utf-8
# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos, pi  # , array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import random
import time

LENGTH_TRACE = 50000
GRAVITATIONAL_CONSTANT = 9.8  # acceleration due to gravity, in m/s^2


class Pendulum(object):
    rad = pi / 180.

    def __init__(self, length=1.0, mass=1.0, angel=180.0, angelvelocity=0):
        self.length = length
        self.mass = mass
        self.angel = angel * self.rad
        self.angelvelocity = angelvelocity * self.rad

    def interact(self, otherPendulum):
        pass


class MultiPendulum(object):
    pass

# angel in degrees, angular velocities in degrees per "second"
Pendulum1 = Pendulum(length=1, mass=1.0, angel=179.5 + random.random())
Pendulum2 = Pendulum(length=1, mass=1.0)
# Pendulum3 = Pendulum(length=0.3, mass=1.0)


def derivs(state, t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = ((Pendulum1.mass + Pendulum2.mass) * Pendulum1.length -
            Pendulum2.mass * Pendulum1.length * cos(del_) * cos(del_))
    dydx[1] = (Pendulum2.mass * Pendulum1.length * state[1] * state[1] * sin(del_) * cos(del_)
               + Pendulum2.mass * GRAVITATIONAL_CONSTANT * sin(state[2]) * cos(del_)
               + Pendulum2.mass * Pendulum2.length * state[3] * state[3] * sin(del_)
               - (Pendulum1.mass + Pendulum2.mass) * GRAVITATIONAL_CONSTANT * sin(state[0])) / den1

    dydx[2] = state[3]

    den2 = (Pendulum2.length / Pendulum1.length) * den1
    dydx[3] = (-Pendulum2.mass * Pendulum2.length * state[3] * state[3] * sin(del_) * cos(del_)
               + (Pendulum1.mass + Pendulum2.mass) * GRAVITATIONAL_CONSTANT * sin(state[0]) * cos(del_)
               - (Pendulum1.mass + Pendulum2.mass) * Pendulum1.length * state[1] * state[1] * sin(del_)
               - (Pendulum1.mass + Pendulum2.mass) * GRAVITATIONAL_CONSTANT * sin(state[2])) / den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.03
t = np.arange(0.0, 2000, dt)


# initial state
state = [Pendulum1.angel, Pendulum1.angelvelocity, Pendulum2.angel, Pendulum2.angelvelocity]

# integrate your ODE using scipy.integrate.
t1 = time.time()
y = integrate.odeint(derivs, state, t)
print("Zeit", time.time() - t1)

x1 = Pendulum1.length * sin(y[:, 0])
y1 = -Pendulum1.length * cos(y[:, 0])

x2 = Pendulum2.length * sin(y[:, 2]) + x1
y2 = -Pendulum2.length * cos(y[:, 2]) + y1

# x3 = Pendulum3.length * sin(y[:, 2]) + x2
# y3 = -Pendulum3.length * cos(y[:, 2]) + y2

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
dots, = ax.plot([], [], '-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    dots.set_data([], [])
    time_text.set_text('')
    return line, dots, time_text


def animate(i):
    if LENGTH_TRACE > i:
        length = i
    else:
        length = LENGTH_TRACE

    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    # time.sleep(0.5)
    line.set_data(thisx, thisy)
    dots.set_data(x2[i - length:i], y2[i - length:i])
    time_text.set_text(time_template % (i * dt))
    return line, dots, time_text


ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=dt, blit=True, init_func=init, repeat=True)

#ani.save('double_pendulum.mp4', fps=15)
plt.show()
