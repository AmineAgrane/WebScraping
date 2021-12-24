import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SipSpider(CrawlSpider):
    """
    When using the CrawlSpider class, 2 important things to keep in mind :
    - We have to set rules to know which links to follow
    - We can't use a parse function named 'parse' because it already exists, we don't want to overwrite it
     so we use another name like parse_items
    """

    name = 'sip'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['https://sipwhiskey.com/']

    rules = (
        # allow any links that contain 'collections' and not 'products' in it.
        Rule(LinkExtractor(allow='collections', deny='products')),
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    )

    def parse_item(self, response):
        yield {
            'brand': response.css('div.vendor a::text').get(),
            'name': response.css('h1.title::text').get(),
            'price': response.css('span.price::text').get()
        }
