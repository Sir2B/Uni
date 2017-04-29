#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from selenium import webdriver

class OfmScraper(object):
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self.open_browser()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        # self.driver.close()

    def open_browser(self):
        # driver = webdriver.Firefox('D:\Portable\Firefox\FirefoxLoader.exe')
        self.driver = webdriver.Chrome(r'D:\Portable\chromedriver_win32\chromedriver.exe')

    def open_ofm(self):
        self.driver.get('http://www.onlinefussballmanager.de/game')

    def login(self):
        self.driver.execute_script("javascript:register_show_login();")

        login_form = self.driver.find_element_by_id("login_form")
        username_form = login_form.find_element_by_id("login")
        password_form = login_form.find_element_by_id("password")

        username, password = self.get_credentials()
        username_form.send_keys(username)
        password_form.send_keys(password)
        username_form.submit()

        login_button = login_form.find_element_by_id("logingrafikbutton")
        login_button.click()

        time.sleep(10)

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



#     @staticmethod
#     def get_config():
#         login = ""
#         password = ""
#         with open('config.cfg', 'r') as conf_file:
#             lines = conf_file.read().splitlines()
#             for line in lines:
#                 words = line.split()
#                 if 'login' in words[0]:
#                     login = words[1]
#                 elif 'password' in words[0]:
#                     password = words[1]
#         return login, password

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
    scraper.open_browser()
    scraper.open_ofm()
    scraper.login()