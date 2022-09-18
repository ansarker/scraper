import scrapy


class GucciItem(scrapy.Item):
    product_name = scrapy.Field()
    category = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
