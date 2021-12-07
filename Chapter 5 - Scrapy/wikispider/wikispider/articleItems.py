from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import Article


class ArticleSpider(CrawlSpider):
    """
    This new ArticleSpider extends the CrawlSpider class. Rather than providing a
    start_requests function, it provides a list of start_urls and allowed_domains.
    This tells the spider where to start crawling from and whether it should follow or
    ignore a link based on the domain.
    """
    name = 'articlesItems'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    """
       A list of rules is also provided. This provides further instructions on which links to
       follow or ignore (in this case, you are allowing all URLs with the regular expression (.*).
    """
    # get only articles links
    rules = [Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=False),]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        #article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was last edited on ', '')
        return article
