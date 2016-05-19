#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Module for solving ordinary differential equations (ODE).
#
# Author:      Tino Wagner
# Creation:    03/2008
# Last Change: $Date: 2008-03-27 11:18:15 +0100 (Do, 27 Mär 2008) $
#           by $Author: tino $
#------------------------------------------------------------------------------

import math

# Global configuration
QUIET = True        # Should the integrators be quiet?
MAX_STEPS = 5000    # How many iterations?


class ODE(object):
    """Base class for ODE solvers."""

    def __init__(self, rhs=None, x=None, t=0, atol=None, rtol=None,
                 min_dt=None):
        """Initializes the ODE using the given system."""

        self._x = x
        self._t = t

        self.atol = atol
        self.rtol = rtol
        self.min_dt = min_dt

        if rhs is None:
            self._rhs = self.rhs
        else:
            self._rhs = rhs

    def set_ode(self, rhs):
        """Set right hand side function of the system."""

        self._rhs = rhs

    def set_initial(self, x, t=0):
        """Set initial conditions."""

        self._x = x
        self._t = t

    def rhs(self, x, t):
        """Default RHS.
        x' = rhs(x, t)
        """

        return []

    def integrate(self, dt):
        pass


class Euler(ODE):
    """Solves ODE using straight-forward Euler method."""

    def __init__(self, rhs=None, x=None, t=0, atol=None, rtol=None,
                 min_dt=None, steps=20):
        super(Euler, self).__init__(rhs, x, t, atol, rtol, min_dt)

        self.steps = steps # number of integration steps between t and t + dt

    def step(self, dt, x0=None, t0=None):
        """Do ODE integration step using Euler."""

        t = self._t if t0 is None else t0
        x = self._x if x0 is None else x0
        n = len(x)

        k1 = self._rhs(x, t) # the one and only step

        x_temp = [x[i] + dt * k1[i] for i in xrange(0, n)]

        return x_temp

    def integrate(self, dt):
        """Integrate ODE."""

        n_steps = self.steps
        dt_i = dt/n_steps

        for i in xrange(0, n_steps):
            self._x = self.step(dt_i)
            self._t += dt_i

        return self._x


class RungeKutta(ODE):
    """Solves ODE using 4th order Runge-Kutta."""

    def __init__(self, rhs=None, x=None, t=0, atol=None,
                 rtol=None, min_dt=None, steps=15):
        super(RungeKutta, self).__init__(rhs, x, t, atol, rtol, min_dt)

        self.steps = steps # number of integration steps between t and t + dt

    def step(self, dt, x0=None, t0=None):
        """Do ODE integration step using Runge-Kutta."""

        t = self._t if t0 is None else t0
        x = self._x if x0 is None else x0
        n = len(x)

        k1 = self._rhs(x, t) # step 1

        x_temp = [x[i] + dt * k1[i] / 2 for i in xrange(0, n)]
        k2 = self._rhs(x_temp, t + dt/2) # step 2

        x_temp = [x[i] + dt * k2[i] / 2 for i in xrange(0, n)]
        k3 = self._rhs(x_temp, t + dt/2) # step 3

        x_temp = [x[i] + dt * k3[i] for i in xrange(0, n)]
        k4 = self._rhs(x_temp, t + dt) # step 4

        x_temp = [x[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 \
                  for i in xrange(0, n)]

        return x_temp

    def integrate(self, dt):
        """Integrate ODE."""

        n_steps = self.steps
        dt_i = dt/n_steps

        for i in xrange(0, n_steps):
            self._x = self.step(dt_i)
            self._t += dt_i

        return self._x


class DormandPrince(ODE):
    """Solves ODE using 5th order Dormand-Prince Runge-Kutta method."""

    def __init__(self, rhs=None, x=None, t=0, atol=None, rtol=None,
                 min_dt=None):
        super(DormandPrince, self).__init__(rhs, x, t, atol, rtol, min_dt)

    def step(self, dt, x0 = None, t0 = None):
        """Do ODE integration step using Dormand-Prince Runge-Kutta method."""

        # Dormand-Prince 5(4) parameters from "Numerical Recipes"
        c2, c3, c4, c5 = (1./5, 3./10, 4./5, 8./9)
        a21 = 1./5
        a31, a32 = (3./40, 9./40)
        a41, a42, a43 = (44./45, -56./15, 32./9)
        a51, a52, a53, a54 = (19372./6561, -25360./2187, 64448./6561, \
                              -212./729)
        a61, a62, a63, a64, a65 = (9017./3168, -355./33, 46732./5247, \
                                   49./176, -5103./18656)
        a71, a72, a73, a74, a75, a76 = (35./384, 0., 500./1113, 125./192, \
                                        -2187./6784, 11./84)
        # coefficients for 5th order system
        b1, b2, b3, b4, b5, b6, b7 = (35./384, 0., 500./1113, 125./192, \
                                      -2187./6784, 11./84, 0.)
        # coefficients for reduced (4th order) system
        b1r, b2r, b3r, b4r, b5r, b6r, b7r = (5179./57600, 0., 7571./16695, \
                                393./640, -92097./339200, 187./2100, 1./40)


        t = self._t if t0 is None else t0
        x = self._x if x0 is None else x0
        n = len(x)

        k1 = self._rhs(x, t) # step 1

        x_temp = [x[i] + dt * a21 * k1[i] for i in xrange(0, n)]
        k2 = self._rhs(x_temp, t + dt * c2) # step 2

        x_temp = [x[i] + dt * (a31 * k1[i] + a32 * k2[i])
                  for i in xrange(0, n)]
        k3 = self._rhs(x_temp, t + dt * c3) # step 3

        x_temp = [x[i] + dt * (a41 * k1[i] + a42 * k2[i] + a43 * k3[i])
                  for i in xrange(0, n)]
        k4 = self._rhs(x_temp, t + dt * c4) # step 4

        x_temp = [x[i] + dt * \
                  (a51 * k1[i] + a52 * k2[i] + a53 * k3[i] + a54 * k4[i])
                  for i in xrange(0, n)]
        k5 = self._rhs(x_temp, t + dt * c5) # step 5

        x_temp = [x[i] + dt * \
                  (a61 * k1[i] + a62 * k2[i] + a63 * k3[i] + a64 * k4[i] + \
                   a65 * k5[i])
                  for i in xrange(0, n)]
        k6 = self._rhs(x_temp, t + dt) # step 6

        # 5th order solution
        x_t = [x[i] + dt * \
               (b1 * k1[i] + b2 * k2[i] + b3 * k3[i] + b4 * k4[i] + \
                b5 * k5[i] + b6 * k6[i])
               for i in xrange(0, n)]

        # w/o error if not tolerances given
        if self.atol is None and self.rtol is None:
            return (x_t, None)

        x_temp = [x[i] + dt * \
                  (a71 * k1[i] + a72 * k2[i] + a73 * k3[i] + a74 * k4[i] + \
                   a75 * k5[i] + a76 * k6[i])
                  for i in xrange(0, n)]
        # step 7 - can be optimized! first same as last (p. 913)
        k7 = self._rhs(x_temp, t + dt)

        # 4th order solution
        x_tr = [x[i] + dt * (b1r * k1[i] + b2r * k2[i] + b3r * k3[i] + \
                             b4r * k4[i] + b5r * k5[i] + b6r * k6[i] + \
                             b7r * k7[i])
                for i in xrange(0, n)]

        def norm(vec): # calculate error
            return math.sqrt(sum([x**2 for x in vec]))

        xx = x_t if norm(x_t) > norm(x) else x
        # scale = atol + max(x_t, x) * rtol
        scale = [self.atol + abs(self.rtol * x_i) for x_i in xx]
        # delta = abs(x_t - x_tr) <= scale
        delta = [abs(x_t[i] - x_tr[i]) for i in xrange(0, n)]
        # err
        err = math.sqrt(sum([(delta[i] / scale[i]) ** 2
                             for i in xrange(0, n)]) / n)

        return (x_t, err)

    def integrate(self, dt):
        """Controls ODE integration."""

        # if no tolerances are given, only do the step dt
        if self.atol is None and self.rtol is None:
            (x, err) = self.step(dt)
            self._x = x
            self._t += dt
            return self._x

        h = dt # help step
        target_t = self._t + dt # target time

        step_cnt = 0
        while step_cnt < MAX_STEPS:
            step_cnt += 1

            if (self._t + h) > target_t:
                break # break if under target time

            (x, err) = self.step(h)

            if not QUIET:
                print "New x calculated using h = %f." % h

            if err < 1:
                self._x = x
                self._t += h

                if not QUIET:
                    print "Integration error = %.2f < 1" % err

            else:
                # safety for calculation of new step width
                safe = 0.9
                h *= safe * math.pow(err, -0.2)

                if not QUIET:
                    print "x dropped. New h: %f" % h

        # remaining step
        hh = target_t - self._t

        # if remaining step > last h => use new h = min_step
        if hh > h:
            print "MAX_STEPS = %i used." % MAX_STEPS

            if self.min_dt is not None:
                print "Doing remaining steps using min_dt = %.2f" \
                       % self.min_dt
                while (self._t+self.min_dt < target_t):
                    (x, err) = self.step(self.min_dt)
                    self._x = x
                    self._t += self.min_dt

        # remaining step
        hh = target_t - self._t

        if not QUIET:
            print "Last h: %f" % hh

        (x, err) = self.step(hh)
        self._x = x
        self._t += hh

        return self._x


# ODE solver using scipy's odeint
try:
    from scipy.integrate import odeint

    class ODEint(ODE):

        def __init__(self, rhs=None, x=None, t=0, atol=None, rtol=None,
                     min_dt=None):
            super(ODEint, self).__init__(rhs, x, t, atol, rtol, min_dt=None)

        def integrate(self, dt):
            """Integrate ODE using Scipy solvers."""

            self._x = odeint(self._rhs, self._x, [0, dt],
                             atol=self.atol, rtol=self.rtol)[-1]
            self._t += dt

            return self._x

except ImportError:
    print "ODE: Scipy integrator not available."


# Set a default integrator.
DefaultIntegrator = DormandPrince


if __name__ == '__main__':
    # solve sample ODE: x'' + x = 0
    # => x' = u
    # => u' = -x

    def diff(x, t):
        return [x[1], -x[0]]

    atol = rtol = 1e-10

    odes = [Euler(diff, [1.0, 0]), RungeKutta(diff, [1.0, 0]),
            DormandPrince(diff, [1.0, 0], atol=atol, rtol=rtol)]

    try:
        odes += [ODEint(diff, [1.0, 0], atol = atol, rtol = rtol)]
    except:
        print "Skipping ODEint test."

    for ode in odes:
        print repr(ode)
        print "cos(pi): %.10f" % ode.integrate(math.pi)[0]
