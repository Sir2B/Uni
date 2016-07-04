import scrapy


class KickerSpider(scrapy.Spider):
    name = "kicker"
    allowed_domains = ["www.kicker.de"]
    start_urls = ["http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2015-16/spieltag.html"]

    def parse(self, response):
        print(response)
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
