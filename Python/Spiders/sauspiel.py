#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess
import subprocess
import pylab


class SauspielSpider(scrapy.Spider):
    name = "sauspiel"
    allowed_domains = ["sauspiel.de"]
    start_urls = ["https://www.sauspiel.de/login"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'login': 'Sir2B', 'password': 'QB87Bvd^FvGWH3h7w*'},
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
        for sel in response.selector.xpath('//ul/li[@class="profile-stats__list-item"]').xpath('text()'):
            text = sel.extract().encode('utf-8')
            if 'Momentan bei P' in text:
                points = text.split()[3]
            if 'insgesamt, davon' in text:
                if games_count == 0:
                    games_count = text.split()[0]
        self.append_stat(points + games_count + '\n', "stats.txt")

    @staticmethod
    def save_page(response, filename):
        # filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

    @staticmethod
    def append_stat(text, filename):
        line = subprocess.check_output(['tail', '-1', filename])
        if text != line:
            with open(filename, 'a') as f:
                f.write(text)
            draw_plot()


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SauspielSpider)
process.start()


def draw_plot():
    filename = "stats.txt"
    data = pylab.loadtxt(filename, delimiter=',', dtype=int)
    y_data = data[:, 0]
    x_data = data[:, 1]
    pylab.plot(x_data, y_data, '-o')
    # pylab.show()
    pylab.savefig('plot.png')
    # pylab.legend()
    # pylab.title("Title of Plot")
    # pylab.xlabel("X Axis Label")
    # pylab.ylabel("Y Axis Label")
    pylab.close()
