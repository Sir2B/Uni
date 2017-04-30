#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

# from ../../Bots/Telegram/Raborutzi import Raborutzi

class OfmScraper(object):
    def __init__(self):
        self.driver = None
        self.remaining_days = []

    def __enter__(self):
        self.open_browser()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.driver.close()

    def open_browser(self, browser="chrome"):
        browser = browser.lower()
        if browser == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
        elif browser == "chrome":
            self.driver = webdriver.Chrome()

    def open_ofm(self):
        self.driver.get('http://www.onlinefussballmanager.de/game')
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "registergrafikbutton"))
        )

    def login(self):
        self.driver.execute_script("javascript:register_show_login();")

        login_form = self.driver.find_element_by_id("login_form")
        username_form = login_form.find_element_by_id("login")
        password_form = login_form.find_element_by_id("password")

        username, password = self.get_credentials()
        username_form.send_keys(username)
        password_form.send_keys(password)
        username_form.submit()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "frameset"))
        )

    def scrap_team_page(self):
        self.driver.get("http://www.onlinefussballmanager.de/team/players.php")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "playerTable"))
        )
        table = self.driver.find_element_by_id("playerTable")
        players = table.find_elements_by_css_selector("tr.odd") + table.find_elements_by_css_selector("tr.even")
        for player in players:
            days = int(player.find_elements_by_css_selector("td")[-2].text)
            self.remaining_days.append(days)
        if min(self.remaining_days) < 2:
            print("Warning! Contract expires")

    @staticmethod
    def get_credentials():
        login = ""
        password = ""
        with open('credentials', 'r') as cred_file:
            lines = cred_file.read().splitlines()
            for line in lines:
                words = line.split()
                if 'login' in words[0]:
                    login = words[1]
                elif 'password' in words[0]:
                    password = words[1]
        return login, password



    @staticmethod
    def get_config():
        login = ""
        password = ""
        with open('config.cfg', 'r') as conf_file:
            lines = conf_file.read().splitlines()
            for line in lines:
                words = line.split()
                if 'login' in words[0]:
                    login = words[1]
                elif 'password' in words[0]:
                    password = words[1]
        return login, password

    @staticmethod
    def save_page(self, filename):
        # filename = response.url.split("/")[-2] + '.html'
        subfolder = "temp"
        filename_path = os.path.join(subfolder, filename)
        with open(filename_path, 'wb') as html_file:
            html_file.write(self.driver.page_source)

#     def append_stat(self, text, filename):
#         line = subprocess.check_output(['tail', '-1', self.absolut_path(filename)])
#         if not self.are_values_equal(line, text):
#             with open(filename, 'a') as stat_file:
#                 stat_file.write(text)
#             # self.draw_plot()

#     def get_actual_time(self):
#         return time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime())

#     # def draw_plot(self):
#     #     self.logger.info("Save the Plot to file")
#     #     data_filename = "stats.txt"
#     #     plot_filename = "plot.png"
#     #     data = pylab.loadtxt(self.absolut_path(data_filename) , delimiter=',', dtype=int)
#     #     self.logger.info(data)
#     #     y_data = data[:, 0]
#     #     x_data = data[:, 1]
#     #     pylab.plot(x_data, y_data, '-')
#     #     # pylab.show()
#     #     pylab.savefig(self.absolut_path(plot_filename))
#     #     # pylab.legend()
#     #     # pylab.title("Title of Plot")
#     #     # pylab.xlabel("X Axis Label")
#     #     # pylab.ylabel("Y Axis Label")
#     #     pylab.close()

#     @staticmethod
#     def absolut_path(filename):
#         return os.path.join(os.getcwd(), filename)

if __name__ == "__main__":
    scraper = OfmScraper()
    scraper.open_browser("firefox")
    scraper.open_ofm()
    scraper.login()
    scraper.scrap_team_page()