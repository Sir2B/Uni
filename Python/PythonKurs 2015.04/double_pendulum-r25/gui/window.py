#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Simple GUI window class.
#
# Author:      Tino Wagner
# Creation:    03/2008
# Last Change: $Date: 2008-03-27 11:24:27 +0100 (Do, 27 Mär 2008) $
#           by $Author: tino $
#------------------------------------------------------------------------------

import pyglet
from pyglet import font
from pyglet import event
from pyglet.gl import *


class Window(event.EventDispatcher):
    """Provides a base class for windows.
    """

    def __init__(self, parent, title="Window", position=None,
                 constraints=(300, 250)):
        """Creates the window."""

        super(Window, self).__init__()

        # If no position is given, center the window.
        if position is None:
            self.x = (parent.width - constraints[0]) / 2
            self.y = (parent.height - constraints[1]) / 2
        else:
            self.x, self.y = position

        self.parent = parent
        self.title = title
        self.width, self.height = constraints

        # title bar dragging
        self._is_dragging = False
        self._drag_x, self._drag_y = (0, 0)

        # Load a font for the titlebar.
        self._titlebarheight = 15
        self.font = font.load(None, self._titlebarheight * 0.9, dpi=72)

        # manage widgets as a list
        self.widgets = []

        parent.push_handlers(self)

    def add_widget(self, widget):
        """Add a widget to the window.
        This will cause the window to call the drawing routines and
        event handlers.
        """
        self.widgets.append(widget)

    def on_mouse_press(self, x, y, buttons, modifiers):
        """Handle mouse presses."""

        y = self.parent.height - y # swap up and down

        # check if pointer is in title bar
        if (self.x < x < self.x+self.width and
            self.y < y < self.y+self._titlebarheight and
            buttons & pyglet.window.mouse.LEFT):
            # start dragging
            self._drag_x, self._drag_y = self.x, self.y
            self._is_dragging = True
            return event.EVENT_HANDLED

        # check if pointer clicked a widget
        # window coordinates
        x = x - self.x
        y = y - (self.y + self._titlebarheight)
        for widget in self.widgets:
            if widget.is_under_pointer(x, y): # widget coordinates!
                widget.on_mouse_press(x - widget.x, y - widget.y,
                                      buttons, modifiers)
                return event.EVENT_HANDLED

        return event.EVENT_UNHANDLED

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """Handle mouse dragging."""

        return self.on_mouse_motion(x, y, dx, dy)

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse move while dragging."""

        if self._is_dragging:
            # don't move windows out of the parent window:
            remain = 15
            if self.x <= self.parent.width-remain and dx > 0: # right
                self.x += dx
            elif self.x >= -self.width+remain and dx < 0: # left
                self.x += dx

            if self.y >= 0 and dy > 0: # up
                self.y -= dy
            elif self.y <= self.parent.height-remain and dy < 0: # down
                self.y -= dy

            return event.EVENT_HANDLED

        # window coordinates
        x = x - self.x
        y = self.parent.height - y - (self.y + self._titlebarheight)
        for widget in self.widgets: # widget coordinates!
            widget.on_mouse_motion(x - widget.x, y - widget.y, dx, dy)

        return event.EVENT_UNHANDLED

    def on_mouse_release(self, x, y, buttons, modifiers):
        """Handle mouse button releases."""

        if self._is_dragging and buttons & pyglet.window.mouse.LEFT:
            self._is_dragging = False
            return event.EVENT_HANDLED

        # window coordinates
        x = x - self.x
        y = self.parent.height - y - (self.y + self._titlebarheight)
        for widget in self.widgets: # widget coordinates!
            widget.on_mouse_release(x - widget.x, y - widget.y,
                                    buttons, modifiers)

        return event.EVENT_UNHANDLED

    def draw(self):
        """Draw the window."""

        glLoadIdentity()

        # turn on blending
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # title bar
        glColor4f(1, 1, 1, 0.4)
        glRectf(self.x, self.parent.height - self.y, self.x + self.width,
                self.parent.height - (self.y + self._titlebarheight))
        # title text
        x = self.x + self.width / 2
        y = self.parent.height - (self.y + self._titlebarheight / 2)
        titlebar_text = font.Text(self.font, text=self.title, x=x, y=y,
                                  halign=font.Text.CENTER,
                                  valign=font.Text.CENTER)
        titlebar_text.color = (1, 1, 1, 0.9)
        titlebar_text.draw()

        # draw the window
        glColor4f(0.2, 0.2, 0.2, 0.7)
        glRectf(self.x, self.parent.height - (self.y + self._titlebarheight),
                self.x + self.width,
                self.parent.height - (self.y + self.height))

        # draw white border around the window
        glColor4f(1, 1, 1, 0.7)
        glBegin(GL_LINE_STRIP)
        glVertex3f(self.x, self.parent.height - self.y, 0)
        glVertex3f(self.x + self.width, self.parent.height - self.y, 0)
        glVertex3f(self.x + self.width,
                   self.parent.height - self.y - self.height, 0)
        glVertex3f(self.x, self.parent.height - self.y - self.height, 0)
        glVertex3f(self.x, self.parent.height - self.y, 0)
        glEnd()

        # now draw the window contents

        # swap up and down
        glPushMatrix()
        glTranslatef(0.0, self.parent.height, 0)
        glScalef(1, -1, 1)
        # translate into the window
        glTranslatef(self.x, self.y + self._titlebarheight, 0)
        self.draw_contents() # draw window contents (buttons, labels, etc.)
        glPopMatrix()

    def draw_contents(self):
        """Will draw the window contents, such as widgets."""

        for widget in self.widgets:
            widget.draw()


if __name__ == '__main__':
    # create basic window
    import widgets

    class TestWindow(Window):

        def __init__(self, parent, title="", position=None,
                     constraints=(300, 200), pendulum=None):
            super(TestWindow, self).__init__(parent, title, position,
                                             constraints)

            # add a label
            self.add_widget(widgets.Label(self,
                                          text=u"This is a basic label.",
                                          position=(10, 10),
                                          constraints=(150, 15)))

            # add a slider
            self.slider = widgets.Slider(self,
                                         position=(10, 30),
                                         constraints=(280, 15),
                                         initial_value=135,
                                         span=(100, 200))
            self.add_widget(self.slider)

            # and a sample slider handler
            self.slider.set_value_handler(self.slider_change)
            self.label = widgets.Label(self, position=(10, 55),
                                       constraints=(280, 15))
            self.label.set_color(0, 1, 0)
            self.add_widget(self.label)
            self.slider_change()

            # add a button
            self.button_clicks = 0
            self.button = widgets.Button(self, text="0", position=(10, 80),
                                         constraints=(50, 15))
            self.button.set_handler(self.button_click)
            self.add_widget(self.button)

        def button_click(self):
            self.button_clicks += 1
            self.button.text = "%i" % self.button_clicks # update button text

        def slider_change(self):
            self.label.text = "Selected slider value: %.5f" % self.slider.value

    # just open two window for testing purposes only
    win = pyglet.window.Window()
    first = TestWindow(win, title="First", position=(15, 15))
    second = TestWindow(win, title="Second", position=(300, 250))

    while not win.has_exit:
        win.dispatch_events()
        win.clear()
        first.draw()
        second.draw()
        win.flip()
