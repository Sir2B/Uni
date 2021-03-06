import telebot
import pyowm
import RPi.GPIO as GPIO
import schedule
import time
import datetime

from credentials import Credentials


class Raborutzi(object):
    def __init__(self, credentials_path='.credentials', window_gpis=[]):
        self.forecaster = None
        self.UPDATE_FORECAST_TIME = 60 * 60  # every hour
        self.CHECK_TIME = 2 * 60 # every 2 minutes
        self.credentials = Credentials(credentials_path)

        self.bot = telebot.TeleBot(self.credentials.TOKEN, threaded=False)
        self.send("Bot started.")
        self.owm = pyowm.OWM(self.credentials.OPEN_WEATHER_MAP)

        self.window_gpis = window_gpis
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(window_gpis, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def start_scheduler(self):
        schedule.every(self.UPDATE_FORECAST_TIME).seconds.do(self.update_forecast)
        schedule.every(self.CHECK_TIME).seconds.do(self.check)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def send(self, text):
        self.bot.send_message(self.credentials.USERID, text)

    def update_forecast(self):
        self.send("updating forecast")
        self.forecaster = self.owm.three_hours_forecast("Tulling,de")

    def is_it_raining(self):
        if not self.forecaster:
            self.update_forecast()
        self.weather = self.forecaster.get_weather_at(datetime.datetime.now())
        self.rain = self.weather.get_rain()['3h']
        return self.rain > 0

    def is_one_window_open(self):
        for gpi in self.window_gpis:
            if GPIO.input(gpi):
                return True
        return True

    def check(self):
        if self.is_one_window_open() and self.is_it_raining():
            warning = "Warning: It's raining and the window is open.\n"
            warning += "Weather: {}; Rain: {} mm".format(self.weather.get_detailed_status(), self.rain)
            self.send(warning)


if __name__ == "__main__":
    obj = Raborutzi()  # window_gpis=[25,7])
    obj.start_scheduler()
    # obj.check()
