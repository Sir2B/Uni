#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Simulation eines Einfachpendels
#
# Author:      Tino Wagner
# Creation:    03/2008
# Last Change: $Date: 2008-03-27 09:25:32 +0100 (Do, 27 Mär 2008) $
#           by $Author: tino $
#------------------------------------------------------------------------------

from math import pi, sin, cos, sqrt

from pyglet.gl import *

# ODE-Modul einbinden
import ode

# Konstanten importieren
from constants import g


class SinglePendulum(object):

    def __init__(self, phi=0.0, length=1.0):
        self.ode = ode.DefaultIntegrator(rhs=self.diff)
        self.reset(phi, length)

    def reset(self, phi, length):
        """Setzt Simulation anhand der übergebenen Parameter zurück."""

        self.phi = phi
        self.length = length
        # Anfangsbedingungen setzen
        self.ode.set_initial([phi, 0])
        self.y_t = [phi, 0]

    def draw(self):
        """Zeichnet Pendel und Pendelmasse."""

        phi = self.y_t[0]

        # Faden zeichnen
        glColor3f(1, 1, 1)
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(self.length * sin(phi), self.length * cos(phi))
        glEnd()

        # Pendelmasse zeichnen
        glColor3f(1, 0, 0)
        glTranslatef(self.length * sin(phi), self.length * cos(phi), 0)
        quadric = gluNewQuadric()
        gluDisk(quadric, 0.0, 0.2, 30, 1)

    def diff(self, y, t):
        """Beschreibt die Differentialgleichung: phi'' + g/l * sin(phi) = 0
        (1 Gleichung 2. Ordnung)
        => 2 gekoppelte DGLs zweiter Ordnung
        phi' = phidot
        phidot' = -g/l * sin(phi)
        """

        return [y[1], -g / self.length * sin(y[0])]

    def update(self, dt):
        """Löst die DGL zu einem zukünftigen Zeitpunkt dt."""

        if dt == 0:
            return

        self.y_t = self.ode.integrate(dt) # DGL lösen
