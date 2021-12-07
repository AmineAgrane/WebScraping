import scrapy


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
    name = "drone"

    # list of urls that reprsent the starting point of the spider
    start_urls = ['https://www.jessops.com/drones']



    def parse(self, response):
        title = response.css('title::text').get()
        initial_url = 'https://www.jessops.com/'

        for drone in response.css('div.details-pricing'):
            # try:
                yield {
                    'title' : drone.css('h4 a::text').get(),
                    'price':  drone.css('p.price.larger::text').get().replace('£','').replace(',',''),
                    'link':  initial_url+drone.css('h4 a::attr(href)').get(),
                }