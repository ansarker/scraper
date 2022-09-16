import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    pagecount = scrapy.Field()
    year = scrapy.Field()
    img_url = scrapy.Field()
