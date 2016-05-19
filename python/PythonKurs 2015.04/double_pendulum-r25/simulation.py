#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Startet die Simulation.
#
# Author:      Tino Wagner
# Creation:    03/2008
# Last Change: $Date: 2008-03-27 10:56:28 +0100 (Do, 27 Mär 2008) $
#           by $Author: tino $
#------------------------------------------------------------------------------

import sys
from math import pi

from pyglet.gl import *
from pyglet import window, clock, font

# GUI importieren
import gui.window
from gui.widgets import Label, Slider, Button

# Pendel importieren
from single_pendulum import SinglePendulum
from double_pendulum import DoublePendulum


class SettingsWindow(gui.window.Window):
    """Fenster zur Änderung der Versuchsparameter."""

    def __init__(self, parent, title="Einstellungen: Doppelpendel",
                position=None, constraints=(285, 200), pendulum=None):
        super(SettingsWindow, self).__init__(parent, title,
                                             position, constraints)

        # Referenz auf Pendel speichern
        self._pendulum = pendulum

        # Simulation gestoppt?
        self.stopped = False

        # Winkel
        self.add_widget(Label(self, text=u"Φ₁ [°]:", position=(10, 10),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.phi1slider = Slider(self, position=(85, 10),
                                 constraints=(190, 15),
                                 initial_value=90, span=(0, 360))
        self.add_widget(self.phi1slider)
        self.add_widget(Label(self, text=u"Φ₂ [°]:", position=(10, 35),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.phi2slider = Slider(self, position=(85, 35),
                                 constraints=(190, 15),
                                 initial_value=180, span=(0, 360))
        self.add_widget(self.phi2slider)

        # Längen
        self.add_widget(Label(self, text=u"l₁ [m]:", position=(10, 60),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.l1slider = Slider(self, position=(85, 60),
                               constraints=(190, 15),
                               initial_value = 4, span = (0.1, 10))
        self.add_widget(self.l1slider)
        self.add_widget(Label(self, text=u"l₂ [m]:", position=(10, 85),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.l2slider = Slider(self, position=(85, 85),
                               constraints=(190, 15),
                               initial_value=5, span=(0.1, 10))
        self.add_widget(self.l2slider)

        # Massen
        self.add_widget(Label(self, text=u"m₁ [kg]:", position=(10, 110),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.m1slider = Slider(self, position=(85, 110),
                               constraints=(190, 15),
                               initial_value=5, span=(0.1, 10))
        self.add_widget(self.m1slider)
        self.add_widget(Label(self, text=u"m₂ [kg]:", position=(10, 135),
                              constraints=(70, 15), align=font.Text.RIGHT))
        self.m2slider = Slider(self, position=(85, 135),
                               constraints=(190, 15),
                               initial_value=10, span=(0.1, 10))
        self.add_widget(self.m2slider)

        # Aktualisierungs-Aktion für die Slider
        self.phi1slider.set_value_handler(self.slider_update)
        self.phi2slider.set_value_handler(self.slider_update)
        self.l1slider.set_value_handler(self.slider_update)
        self.l2slider.set_value_handler(self.slider_update)
        self.m1slider.set_value_handler(self.slider_update)
        self.m2slider.set_value_handler(self.slider_update)

        # Buttons
        self.startbutton = Button(self, position=(10, 160),
                                  constraints=(50, 15))
        self.update_start_button()
        self.startbutton.set_handler(self.start_action)
        self.add_widget(self.startbutton)
        self.resetbutton = Button(self, text="Reset", position=(70, 160),
                                  constraints=(50, 15))
        self.resetbutton.set_handler(self.reset)
        self.add_widget(self.resetbutton)

    def update_start_button(self):
        if self.stopped:
            self.startbutton.text = "Start"
        else:
            self.startbutton.text = "Stop"

    def start_action(self):
        self.stopped = not self.stopped
        self.update_start_button()

    def reset(self):
        phi1 = self.phi1slider.value / 180.0 * pi
        phi2 = self.phi2slider.value / 180.0 * pi
        length1 = self.l1slider.value
        length2 = self.l2slider.value
        mass1 = self.m1slider.value
        mass2 = self.m2slider.value
        self._pendulum.reset(phi1, phi2, length1, length2, mass1, mass2)

    def slider_update(self):
        if self.stopped:
            self.reset()


class PendulumWindow(window.Window):

    def __init__(self, caption="Simulation"):
        """Initialisiert das Fenster."""

        # Fenster öffnen
        try:
            config = Config(sample_buffers=1, samples=1, double_buffer=True)
            super(PendulumWindow, self).__init__(config=config,
                                                 resizable=True,
                                                 caption=caption)
        except:
            super(PendulumWindow, self).__init__(resizable=True,
                                                 caption=caption)

        # Schrift laden
        self.font_sans = font.load(None, 16)

        # FPS
        self.fps_display = clock.ClockDisplay()

        # Pendel aufhängen
        self.single_pendulum = SinglePendulum(length=9.0, phi=pi / 5)
        self.double_pendulum = DoublePendulum()

        # Einstellungsfenster
        self.settings_window = SettingsWindow(self,
                                              pendulum=self.double_pendulum,
                                              position=(15, 15))
        self.settings_window.reset()

    def on_resize(self, width, height):
        """Auf Veränderung der Fenstergröße reagieren."""

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def run(self):
        """Mainloop. Arbeitet Ereignisse ab."""

        while not self.has_exit:
            self.dispatch_events()
            self.update()
            self.draw()
            self.settings_window.draw()
            self.flip()

    def update(self):
        """Aktualisiert den Versuchsaufbau."""

        dt = clock.tick()
        self.single_pendulum.update(dt)
        # nur aktualisieren, wenn Simulation läuft
        if not self.settings_window.stopped:
            self.double_pendulum.update(dt)

    def draw(self):
        """Zeichnet das Fenster."""

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glPushMatrix()
        # oben und unten vertauschen (pyglet geht von linker unterer
        # Ecke als Nullpunkt aus)
        glTranslatef(0, self.height, 0)
        glScalef(1, -1, 1)

        # Koordinatensystem skalieren
        scale = 0.2 * self.height / 2 - 30

        # Einfachpendel links
        glPushMatrix()
        glTranslatef(0.25 * self.width, self.height / 2, 0)
        glScalef(scale, scale, scale)
        self.single_pendulum.draw()
        glPopMatrix()

        # Doppelpendel rechts
        glPushMatrix()
        glTranslatef(0.75 * self.width, self.height / 2, 0)
        glScalef(scale, scale, scale)
        self.double_pendulum.draw()
        glPopMatrix()

        glPopMatrix()

        # Text darstellen
        t = font.Text(self.font_sans,
                      text="E = %.2f J" % self.double_pendulum.energy,
                      x=self.width - 10, y=10, halign=font.Text.RIGHT)
        t.draw()
        self.fps_display.draw()


if __name__ == '__main__':
    PendulumWindow().run()
    sys.exit(0)
