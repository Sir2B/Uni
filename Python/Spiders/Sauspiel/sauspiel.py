#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import matplotlib
# # Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')

import scrapy
from scrapy.crawler import CrawlerProcess
import subprocess
import pylab
import os
import sys
import time
import logging
from scrapy.utils.log import configure_logging


class SauspielSpider(scrapy.Spider):
    name = "sauspiel"
    allowed_domains = ["sauspiel.de"]
    start_urls = ["https://www.sauspiel.de/login"]
    def __init__(self):
        logging.getLogger('scrapy').setLevel(logging.WARNING)
        logging.getLogger('scrapy').propagate = False

    def parse(self, response):
        login, password = self.get_credentials()
        self.save_page(response, 'before_login.html')
        return scrapy.FormRequest.from_response(
            response,
            formdata={'login': login, 'password': password},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "Spielername oder Kennwort falsch!" in response.body:
            self.logger.error("Login failed")
            return
        else:
            self.save_page(response, 'after_login.html')
            return scrapy.Request('https://www.sauspiel.de/profil', callback=self.parse_page)

    def parse_page(self, response):
        self.save_page(response, 'profil.html')
        points = 0
        games_count = 0
        for sel in response.selector.xpath('//div[@id="profil_stats_punkte"]').xpath('//ul/li').xpath('text()'):
            text = sel.extract().encode('utf-8')
            if 'Momentan bei P' in text:
                points = text.split()[3][:-1]
            if 'insgesamt, davon' in text:
                if games_count == 0:
                    games_count = text.split()[0]
	self.logger.info("Got data: {0} {1}".format(points, games_count))
        self.append_stat("{},{},{}\n".format(points, games_count, self.get_actual_time()), "stats.txt")

    @staticmethod
    def get_credentials():
        login = ""
        password = ""
        with open('credentials', 'r') as f:
            lines = f.read().splitlines() 
            for line in lines:
                l = line.split()
                if 'login' in l[0]:
                    login = l[1]
                elif 'password' in l[0]:
                    password = l[1]
        return login, password

    @staticmethod
    def save_page(response, filename):
        # filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

    def append_stat(self, text, filename):
        line = subprocess.check_output(['tail', '-1', self.absolut_path(filename)])
        if not self.are_values_equal(line, text):
            with open(filename, 'a') as f:
                f.write(text)
            # self.draw_plot()

    def get_actual_time(self):
        return time.strftime("%Y-%m-%d,%H:%M:%S", time.localtime())

    # def draw_plot(self):
    #     self.logger.info("Save the Plot to file")
    #     data_filename = "stats.txt"
    #     plot_filename = "plot.png"
    #     data = pylab.loadtxt(self.absolut_path(data_filename) , delimiter=',', dtype=int)
    #     self.logger.info(data)
    #     y_data = data[:, 0]
    #     x_data = data[:, 1]
    #     pylab.plot(x_data, y_data, '-')
    #     # pylab.show()
    #     pylab.savefig(self.absolut_path(plot_filename))
    #     # pylab.legend()
    #     # pylab.title("Title of Plot")
    #     # pylab.xlabel("X Axis Label")
    #     # pylab.ylabel("Y Axis Label")
    #     pylab.close()

    @staticmethod
    def absolut_path(filename):
        return os.path.join(os.getcwd(), filename)

    @staticmethod
    def are_values_equal(line1, line2):
        line1_array = line1.split(',')
        line2_array = line2.split(',')
        if line1_array[0] != line2_array[0]:
            return False
        if line2_array[1] != line2_array[1]:
            return False
        return True


os.chdir('/home/pi/sauspiel/')
configure_logging(settings=None, install_root_handler=False)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SauspielSpider)

process.start()



