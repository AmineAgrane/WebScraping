import scrapy
# Remove HTML Tags only.
from w3lib.html import remove_tags

# Returns the first non-null/non-empty value from the values received.
from itemloaders.processors import TakeFirst

# the first function is applied to each element. The results of these function are
# concatenated to construct a new iterable, which is then used to apply the second function,
# and so on, until the last function is applied to each value of the list of values
from itemloaders.processors import MapCompose


def remove_currency(value):
    return value.replace('£', '').strip()


class WhiskeyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency), output_processor=TakeFirst())
    link = scrapy.Field()
