import scrapy

class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['http://fake-plants.co.uk/']

    def parse(self, response):
        """
        the first get request is on the 'start_urls' list. we get its content in the reponse object;
        then, we captures all of its inside links with a css selector
        for each link, we call the parse category method
        """
        links = response.css('li.product-category a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_category)

    def parse_category(self, response):
        """
        get the content of each page. for each page we extract and parse the
        category and the name of each product present in that page
        """
        products = response.css('div.astra-shop-summary-wrap')
        for product in products:
            yield {
                'cat': product.css('span.ast-woo-product-category::text').get().strip(),
                'name': product.css('h2.woocommerce-loop-product__title::text').get().strip(),
            }
