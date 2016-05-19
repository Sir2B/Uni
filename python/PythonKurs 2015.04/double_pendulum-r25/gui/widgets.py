#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#------------------------------------------------------------------------------
# Simple widget classes.
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

# Debug mode?
DEBUG = False


class Widget(object):
    """This is the mother of all widgets.
    Provides methods and behaviour each widget should incorporate.
    """

    def __init__(self, parent, position=(0, 0), constraints=(0, 0)):
        """Does basic widget setup."""

        super(Widget, self).__init__()
        self.x, self.y = position
        self.width, self.height = constraints
        self.parent = parent.parent

    def draw(self):
        """Draws the widget."""
        if DEBUG:
            glColor4f(0, 1, 0, 0.1)
            glRectf(self.x, self.y, self.x+self.width, self.y+self.height)

    def is_under_pointer(self, x, y):
        """Check if widget is under mouse pointer.
        Coordinates relative to parent!
        """

        if (self.x < x < self.x+self.width and
                self.y < y < self.y+self.height):
            return True
        else:
            return False

    def on_mouse_press(self, x, y, buttons, modifiers):
        """Handle mouse button press."""

        pass

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse motion on the widget."""

        pass

    def on_mouse_release(self, x, y, buttons, modifiers):
        """Handle mouse button releases."""

        pass


class Label(Widget):
    """Provides a basic label widget."""

    def __init__(self, parent, text="", position=(0, 0),
                 constraints=(50, 15),
                 fontname=None, fontsize=13, align=font.Text.LEFT):
        """Initialize the label."""

        super(Label, self).__init__(parent, position, constraints)

        self.font = font.load(fontname, fontsize, dpi=72) # load font

        self._text = font.Text(self.font, text=text, width=self.width,
                                halign=align, valign=font.Text.CENTER)
        self.set_color(1, 1, 1)

    def get_text(self):
        """Get label text."""

        return self._text.text

    def set_text(self, text):
        """Set label text."""

        self._text.text = text

    text = property(get_text, set_text)

    def set_color(self, r, g, b, a=1):
        """Set the label text color."""

        self._text.color = (r, g, b, a)

    def draw(self):
        """Draw the label."""

        super(Label, self).draw()

        glPushMatrix()
        glTranslatef(self.x, self.y + self.height / 2, 0)
        glScalef(1, -1, 1)
        self._text.draw()
        glPopMatrix()


class Button(Widget):
    """Provide a basic button."""

    def __init__(self, parent, text="", position=(0, 0),
                 constraints=(50, 15)):
        """Initialize the button."""

        super(Button, self).__init__(parent, position, constraints)

        self.label = Label(self, text=text, constraints=constraints,
                           align=font.Text.CENTER)
        self._handler = self.on_click # default button handler
        self._hover = False # mouse over button?

    def set_handler(self, handler):
        """Sets a handler for button presses."""
        self._handler = handler

    def on_click(self):
        """Default button click handler."""

        pass

    def set_text(self, text):
        """Sets the button text."""

        self.label.text = text

    def get_text(self):
        """Returns the button label."""

        return self.label.text

    text = property(get_text, set_text)

    def draw(self):
        """Draws the button."""

        super(Button, self).draw()

        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        # button
        if self._hover:
            glColor4f(0.4, 0.4, 0.4, 0.7)
        else:
            glColor4f(0.2, 0.2, 0.2, 0.7)
        glRectf(0, 0, self.width, self.height)
        # white border
        glColor4f(1, 1, 1, 0.7)
        glBegin(GL_LINE_STRIP)
        glVertex3f(0, 0, 0)
        glVertex3f(self.width, 0, 0)
        glVertex3f(self.width, self.height, 0)
        glVertex3f(0, self.height, 0)
        glVertex3f(0, 0, 0)
        glEnd()
        # button label
        self.label.draw()
        glPopMatrix()

    def on_mouse_press(self, x, y, buttons, modifiers):
        self._handler()

    def on_mouse_motion(self, x, y, dx, dy):
        self._hover = self.is_under_pointer(x + self.x, y + self.y)


class Slider(Widget):
    """Slider with a label."""

    def __init__(self, parent, position=(0, 0), constraints=(180, 15),
                 initial_value=None, span=(0, 100)):
        """Initialize the slider."""

        super(Slider, self).__init__(parent, position, constraints)

        self._span = span

        if initial_value is None:
            self._value = span[0] # preset is the leftmost value
        else:
            self._value = initial_value

        self._is_dragging = False

        self._sliderwidth = 10

        # label for the selected value
        self.display_format = "%.2f"
        self.display = Label(parent,
                             position=(self.width - 55, 0),
                             constraints=(55, 15),
                             text=self.display_format % self._value,
                             align=font.Text.RIGHT)

        # handler for slider
        self._handler = self.on_slider_move

    def get_value(self):
        """Gets current slider value."""
        return self._value

    def set_value(self, value):
        """Sets slider value."""

        self._value = value
        self.display.text = self.display_format % value
        self._handler() # do handler action

    value = property(get_value, set_value)

    def set_value_handler(self, handler):
        """Sets a handler that will be called, if the value has
        been altered."""

        self._handler = handler

    def on_slider_move(self):
        """Default handler for value changes."""

        pass

    def draw(self):
        """Draws the slider."""

        super(Slider, self).draw()

        glPushMatrix()
        glTranslatef(self.x, self.y, 0)
        # draw the slider bar
        glColor4f(1, 1, 1, 0.7)
        lineheight = 0.3 * self.height
        glRectf(self._sliderwidth / 2,
                self.height / 2 - lineheight / 2,
                self.width - self.display.width - self._sliderwidth / 2,
                self.height / 2 + lineheight / 2)

        # draw the slider
        glColor4f(1, 1, 1, 1)
        sliderpos = self.get_slider_pos()
        glRectf(sliderpos,
                self.height / 2 - self._sliderwidth / 2,
                sliderpos + self._sliderwidth,
                self.height / 2 + self._sliderwidth / 2)

        # draw the label
        self.display.draw()
        glPopMatrix()

    def get_slider_pos(self):
        """Gets the absolute (x-)position of the slider."""

        return float(self._value - self._span[0]) / \
                    (self._span[1] - self._span[0]) * \
                    (self.width - self.display.width - self._sliderwidth)

    def set_slider_pos(self, x):
        """Sets the absolute (x-)position of the slider."""

        if x < 0:
            self.value = self._span[0]
        elif x > (self.width - self.display.width - self._sliderwidth):
            self.value = self._span[1]
        else:
            self.value = self._span[0] + float(x) / \
                         (self.width - self.display.width - \
                         self._sliderwidth) * \
                         (self._span[1] - self._span[0])

    def on_mouse_press(self, x, y, buttons, modifiers):
        # check if pointer is on slider
        sliderpos = self.get_slider_pos()
        if (sliderpos < x < sliderpos+self._sliderwidth and
                0 < y < 15):
            self._is_dragging = True
        elif (0 < x < self.width-self.display.width): # clicked on slider bar
            self.set_slider_pos(x - self._sliderwidth / 2)

    def on_mouse_motion(self, x, y, dx, dy):
        if self._is_dragging:
            self.set_slider_pos(x - self._sliderwidth / 2)

    def on_mouse_release(self, x, y, buttons, modifiers):
        if self._is_dragging and buttons & pyglet.window.mouse.LEFT:
            self._is_dragging = False
