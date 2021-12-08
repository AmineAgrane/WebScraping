import scrapy
from whiskey.items import WhiskeyItem
from scrapy.loader import ItemLoader


###### SHELL MODE #######
# first thing to do is type "scrapy shell" so we can access scrapy's interactive shell
# than we use the command 'fetch(url)' so we can have the url content stored in the reponse variable
# we can now execute multiple request on the response variable to test our selector and our program more generaly

# fetch('https://www.whiskyshop.com/scotch-whisky/all')
# products = response.css('div.product-item-info')
# products.css('a.product-item-link')
# for p in products:
#  title = p.css('a.product-item-link::text').get()
#  price = p.css('span.price::text').get().replace('£', '')
#  link  = p.css('a.product-item-link').attrib['href']

class WhiskySpider(scrapy.Spider):
    """ run program  : 'scrapy crawl whisky' (in \PycharmProjects\WebScraping\Scrapy Whiskey\whiskey\)
    export results to json file : 'scrapy crawl whisky -O whisky.json' """

    # Name of the spider to differentiate it from the others
    name = "whisky"

    # list of urls that reprsent the starting point of the spider
    start_urls = ['https://www.whiskyshop.com/scotch-whisky/all']


    def parse(self, response):
        products = response.css('div.product-item-info')

        for product in products:
            loader = ItemLoader(item=WhiskeyItem(), selector=product)
            loader.add_css('name', 'a.product-item-link')
            loader.add_css('price', 'span.price')
            loader.add_css('link', 'a.product-item-link::attr(href)')

            yield loader.load_item()

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def old_parse(self, response):
        products = response.css('div.product-item-info')
        for product in products:
            try:
                yield {
                    'name':  product.css('a.product-item-link::text').get(),
                    'price':  product.css('span.price::text').get().replace('£', ''),
                    'link':   product.css('a.product-item-link').attrib['href'],
                }
            except:
                yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': product.css('a.product-item-link').attrib['href'],
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
