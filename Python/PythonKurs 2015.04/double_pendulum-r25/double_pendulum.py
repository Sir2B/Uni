#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Simulation eines Doppelpendels
#
# Author:      Tino Wagner
# Creation:    03/2008
# Last Change: $Date: 2008-03-27 08:47:51 +0100 (Do, 27 Mär 2008) $
#           by $Author: tino $
#------------------------------------------------------------------------------

from math import pi, sin, cos, sqrt
from collections import deque

from pyglet.gl import *

# ODE-Modul einbinden
import ode

# Konstanten importieren
from constants import g


class DoublePendulum(object):
    def __init__(self, phi1=0.0, phi2=0.0, length1=0.5, length2=0.5,
                 mass1=1.0, mass2=1.0):
        self.ode = ode.DefaultIntegrator(rhs=self.diff, atol=1e-8,
                                         rtol=1e-8, min_dt=1e-2)
        self.reset(phi1, phi2, length1, length2, mass1, mass2)

    def reset(self, phi1, phi2, length1, length2, mass1, mass2):
        """Setzt Simulation zurück."""
        self.length1 = length1
        self.length2 = length2
        self.mass1 = mass1
        self.mass2 = mass2
        self.y_t = [phi1, phi2, 0, 0]  # Anfangsbedingungen setzen
        self.ode.set_initial(self.y_t)
        self._trace = deque()  # Spur löschen

    def draw(self):
        """Zeichnet das Doppelpendel."""

        # Positionen
        phi1 = self.y_t[0]
        phi2 = self.y_t[1]

        # Spur zeichnen
        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_LINE_STRIP)
        for x, y in self._trace:
            glVertex2f(x, y)
        glEnd()

        # Pendel zeichnen
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(self.length1 * sin(phi1), self.length1 * cos(phi1))
        glVertex2f(self.length1 * sin(phi1) + self.length2 * sin(phi2),
                   self.length1 * cos(phi1) + self.length2 * cos(phi2))
        glEnd()

        # Pendelmasse 1
        mass_scale = 0.05
        quadric = gluNewQuadric()
        glColor3f(0.0, 0.0, 1.0)
        glTranslatef(self.length1 * sin(phi1), self.length1 * cos(phi1), 0.0)
        gluDisk(quadric, 0.0, self.mass1 * mass_scale, 30, 1)

        # Pendelmasse 2
        glColor3f(0.0, 1.0, 0.0)
        glTranslatef(self.length2 * sin(phi2), self.length2 * cos(phi2), 0.0)
        gluDisk(quadric, 0.0, self.mass2 * mass_scale, 30, 1)

    @property
    def V(self):
        """Potentielle Energie des Systems."""

        m1, m2 = self.mass1, self.mass2
        l1, l2 = self.length1, self.length2
        return - (m1 + m2) * g * l1 * cos(self.y_t[0]) - m2 * g * l2 * cos(self.y_t[1])

    @property
    def T(self):
        """Kinetische Energie des Systems."""

        return .5 * self.mass1 * (self.length1 ** 2) * (self.y_t[2] ** 2) + \
               .5 * self.mass2 * ((self.length1 ** 2) * (self.y_t[2] ** 2) +
                                  (self.length2 ** 2) * (self.y_t[3] ** 2) +
                                  2 * self.length1 * self.length2 * self.y_t[2] *
                                  self.y_t[3] * cos(self.y_t[0] - self.y_t[1]))

    @property
    def energy(self):
        """Gesamtenergie"""

        return self.T + self.V

    def diff(self, y, t):
        """ Berechnet die rechte Seite der Differentialgleichung
            des Doppelpendels.

        # Belegungen des Vektors
            y[0] = phi1
            y[1] = phi2
            y[2] = phi1'
            y[3] = phi2'
        """

        # Massen
        m1 = self.mass1
        m2 = self.mass2
        M = m1 + m2
        # Längen
        l1 = self.length1
        l2 = self.length2

        # rechte Seiten der DGLs berechnen

        C = cos(y[0] - y[1])  # C = cos(phi1-phi2)
        S = sin(y[0] - y[1])  # S = sin(phi1-phi2)

        phi1dot = y[2]
        phi2dot = y[3]
        phi1dotdot = (m2 * C * (l1 * S * (y[2] ** 2) - g * sin(y[1])) + m2 * l2 * S * (y[3] ** 2) +
                      M * g * sin(y[0])) / (m2 * l1 * (C ** 2) - M * l1)
        phi2dotdot = (m2 * l2 * C * S * (y[3] ** 2) + M * l1 * S * (y[2] ** 2) +
                      M * g * C * sin(y[0]) - M * g * sin(y[1])) / (M * l2 - m2 * l2 * (C ** 2))

        # rechte Seite der DGL zurückgeben
        return [phi1dot,
                phi2dot,
                phi1dotdot,
                phi2dotdot]

    def update(self, dt):
        """Löst die DGL zu einem zukünftigen Zeitpunkt dt."""

        if dt == 0:
            return

        y = self.ode.integrate(dt)  # DGL lösen
        self.y_t = y

        # Punkt zur Spur anfügen
        if len(self._trace) > 1000:  # auf 1000 Wegpunkte beschränken
            self._trace.popleft()
        self._trace.append((self.length1 * sin(self.y_t[0]) +
                            self.length2 * sin(self.y_t[1]),
                            self.length1 * cos(self.y_t[0]) +
                            self.length2 * cos(self.y_t[1])))
