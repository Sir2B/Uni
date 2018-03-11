#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import collections
import datetime

from credentials import Credentials

class OpenWindowDetection(object):
    """ this script analysis the temperature and detects if a temperature is still open and sends then a message"""
    def __init__(self, credentials_path='.credentials'):
        self.message_interval = datetime.timedelta(seconds=10)
        self.window_open = False
        self.last_temps = collections.deque(maxlen=3)
        self.last_message_time = datetime.datetime.now()
        self.credentials = Credentials(credentials_path)
        self.bot = telebot.TeleBot(self.credentials.TOKEN)
        self.bot.send_message(self.credentials.USERID, "Bot started.")

    def new_temperature(self, temp):
        self.last_temps.append(temp)
        if not self.window_open:
            self.window_open = self.check_if_window_was_openend()
        else:
            if self.check_if_window_was_closed():
                self.window_open = False
            else:
                self.send('Fenster ist offen')



    def check_if_window_was_openend(self):
        if len(self.last_temps) != self.last_temps.maxlen:
            return False

        total_diff = self.last_temps[self.last_temps.maxlen-1] - self.last_temps[0]
        diff = []

        for index in range(1, len(self.last_temps)):
            diff.append(self.last_temps[index] - self.last_temps[index-1])

        if total_diff < -1.5 and min(diff) < -0.1:
            return True
        return False

    def check_if_window_was_closed(self):
        total_diff = self.last_temps[self.last_temps.maxlen-1] - self.last_temps[0]
        diff = []

        for index in range(1, len(self.last_temps)):
            diff.append(self.last_temps[index] - self.last_temps[index-1])

        if total_diff > 1.0 and max(diff) > 0.1:
            return True
        return False

    def set_message_interval(self, interval):
        self.message_interval = interval

    def send(self, text):
        if datetime.datetime.now() - self.last_message_time > self.message_interval:
            self.last_message_time = datetime.datetime.now()
            self.bot.send_message(self.credentials.USERID, text)

if __name__ == "__main__":
    import time

    bot = OpenWindowDetection()
    temp = 18
    diff = -1

    while True:
        bot.new_temperature(temp)
        time.sleep(1)
        temp += diff
        if temp <= 0.0:
            diff = +0.2
        if temp > 18.0:
            diff = -1

