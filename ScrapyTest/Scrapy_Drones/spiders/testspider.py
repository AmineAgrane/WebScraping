import scrapy
import request  

###### SHELL MODE #######
# products = response.css('div.product-item-info')
# products.css('a.product-item-link')
# for p in products:
#  title = p.css('a.product-item-link::text').get()
#  price = p.css('span.price::text').get().replace('£', '')
#  link  = p.css('a.product-item-link').attrib['href']


class DroneSpider(scrapy.Spider):
    """
    run program  : 'scrapy crawl whisky' (in \PycharmProjects\WebScraping\Scrapy Whiskey\whiskey\)
    export results to json file : 'scrapy crawl whisky -O whisky.json'
    """
    # Name of the spider to differentiate it from the others
    name = "test"

    # list of urls that reprsent the starting point of the spider
    start_urls = ['https://play.google.com/store/apps/details?id=com.whatsapp/']



    def parse(self, response):
        title = response.css('h1.AHFaub span::text').get()
        developer = response.css('span.T32cc.UAO9ie a::text').get()

        print(title, developer)
        yield title